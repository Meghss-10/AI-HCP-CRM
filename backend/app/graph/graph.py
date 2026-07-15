from typing import TypedDict
from langgraph.graph import StateGraph, END
from app.services.groq_service import llm


class AgentState(TypedDict):
    message: str
    response: str


def run_llm(state: AgentState):

    prompt = f"""
You are an AI assistant for a Healthcare CRM used by pharmaceutical field representatives.

You support FIVE operations:

1. Log Interaction
- Extract interaction details from natural language.
- Return ONLY valid JSON.

2. Edit Interaction
- If the user asks to modify a previous interaction, update only the mentioned fields.
- Keep all other fields unchanged whenever possible.

3. Summarize Interaction
- If the user asks for a summary, return a short professional summary instead of JSON.

4. Recommend Follow-up
- If the user asks what to do next, suggest an appropriate follow-up action.

5. Meeting Insights
- If the user asks for insights, provide key observations and recommendations.

If the request is to LOG or EDIT an interaction,
return ONLY this JSON format:

{{
    "hcp_name":"",
    "interaction_type":"Meeting",
    "interaction_date":"",
    "interaction_time":"",
    "attendees":"",
    "topics_discussed":"",
    "materials_shared":"",
    "samples_distributed":"",
    "sentiment":"Positive",
    "outcomes":"",
    "follow_up":""
}}

Do NOT use markdown.
Do NOT use triple backticks.

User Message:
{state["message"]}
"""

    result = llm.invoke(prompt)

    return {
        "response": result.content
    }


builder = StateGraph(AgentState)

builder.add_node("llm", run_llm)

builder.set_entry_point("llm")

builder.add_edge("llm", END)

graph = builder.compile()