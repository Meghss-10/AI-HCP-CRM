import json
from typing import Any, Dict, Optional

from fastapi import APIRouter
from pydantic import BaseModel

from app.graph.graph import graph


router = APIRouter(
    prefix="/agent",
    tags=["AI Agent"],
)


class ChatRequest(BaseModel):
    message: str
    interaction: Optional[Dict[str, Any]] = None


def has_interaction_data(interaction: Dict[str, Any]) -> bool:
    """Check whether the frontend contains a logged interaction."""
    important_fields = [
        "hcp_name",
        "topics_discussed",
        "materials_shared",
        "samples_distributed",
        "outcomes",
        "follow_up",
    ]

    return any(
        interaction.get(field)
        for field in important_fields
    )


def build_interaction_context(
    interaction: Dict[str, Any],
) -> str:
    """Convert the current Redux interaction into readable context."""
    return f"""
Current logged HCP interaction:

HCP Name: {interaction.get("hcp_name", "")}
Interaction Type: {interaction.get("interaction_type", "")}
Interaction Date: {interaction.get("interaction_date", "")}
Interaction Time: {interaction.get("interaction_time", "")}
Attendees: {interaction.get("attendees", "")}
Topics Discussed: {interaction.get("topics_discussed", "")}
Materials Shared: {interaction.get("materials_shared", "")}
Samples Distributed: {interaction.get("samples_distributed", "")}
Sentiment: {interaction.get("sentiment", "")}
Outcomes: {interaction.get("outcomes", "")}
Follow-up: {interaction.get("follow_up", "")}
"""


def clean_llm_response(response: str) -> str:
    """Remove markdown formatting returned by the LLM."""
    return (
        response
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )


@router.post("/chat")
def chat(request: ChatRequest):

    user_message = request.message.strip()
    lower_message = user_message.lower()

    current_interaction = request.interaction or {}
    interaction_exists = has_interaction_data(
        current_interaction
    )

    # ---------------------------------
    # Summarize Interaction Tool
    # ---------------------------------
    if (
        "summarize" in lower_message
        or "summarise" in lower_message
        or "summary" in lower_message
    ):
        if not interaction_exists:
            return {
                "raw_response":
                    "No interaction details are available to summarize."
            }

        context = build_interaction_context(
            current_interaction
        )

        result = graph.invoke(
            {
                "message": f"""
You are using the Summarize Interaction tool.

Create a short, professional summary of the following
Healthcare Professional interaction.

Do not return JSON.
Do not use markdown code blocks.
Respond naturally in 3 to 5 sentences.

{context}
""",
                "response": "",
            }
        )

        return {
            "raw_response": clean_llm_response(
                result["response"]
            )
        }

    # ---------------------------------
    # Follow-up Recommendation Tool
    # ---------------------------------
    if (
        "suggest follow-up" in lower_message
        or "suggest follow up" in lower_message
        or "recommend follow-up" in lower_message
        or "recommend follow up" in lower_message
        or "next best action" in lower_message
        or "what should i do next" in lower_message
    ):
        if not interaction_exists:
            return {
                "raw_response":
                    "No interaction details are available "
                    "for a follow-up recommendation."
            }

        context = build_interaction_context(
            current_interaction
        )

        result = graph.invoke(
            {
                "message": f"""
You are using the Suggest Follow-up tool.

Based on the following Healthcare Professional interaction,
recommend the most suitable next action for the field
representative.

Do not return JSON.
Do not use markdown code blocks.
Give a concise and practical recommendation.

{context}
""",
                "response": "",
            }
        )

        return {
            "raw_response": clean_llm_response(
                result["response"]
            )
        }

    # ---------------------------------
    # Meeting Insights Tool
    # ---------------------------------
    if (
        "meeting insights" in lower_message
        or "provide insights" in lower_message
        or "give insights" in lower_message
        or "interaction insights" in lower_message
    ):
        if not interaction_exists:
            return {
                "raw_response":
                    "No interaction details are available "
                    "for generating insights."
            }

        context = build_interaction_context(
            current_interaction
        )

        result = graph.invoke(
            {
                "message": f"""
You are using the Meeting Insights tool.

Analyze the following Healthcare Professional interaction.

Provide:
1. One key observation.
2. One potential opportunity.
3. One recommended action.

Do not return JSON.
Do not use markdown code blocks.
Keep the response concise and professional.

{context}
""",
                "response": "",
            }
        )

        return {
            "raw_response": clean_llm_response(
                result["response"]
            )
        }

    # ---------------------------------
    # Log Interaction / Edit Interaction
    # ---------------------------------
    message_for_graph = user_message

    if interaction_exists:
        context = build_interaction_context(
            current_interaction
        )

        message_for_graph = f"""
Existing interaction details:

{context}

User request:
{user_message}

If the user is editing the interaction, return the complete
updated interaction as JSON.

Preserve every existing value unless the user explicitly asks
to modify it.

If the user is logging a completely new interaction, extract
the new interaction details normally.
"""

    result = graph.invoke(
        {
            "message": message_for_graph,
            "response": "",
        }
    )

    response = clean_llm_response(
        result["response"]
    )

    try:
        start = response.find("{")
        end = response.rfind("}")

        if start != -1 and end != -1:
            response = response[start:end + 1]

        data = json.loads(response)

        # Preserve current fields during Edit Interaction
        if interaction_exists:
            merged_data = {
                **current_interaction,
                **{
                    key: value
                    for key, value in data.items()
                    if value not in ["", None]
                },
            }

            return merged_data

        return data

    except Exception as error:
        print("\n========== AGENT JSON ERROR ==========")
        print(error)
        print("\n========== RAW RESPONSE ==========")
        print(response)
        print("======================================\n")

        return {
            "error": str(error),
            "raw_response": response,
        }