from fastapi import APIRouter
from pydantic import BaseModel
from app.graph.graph import graph
import json


router = APIRouter(
    prefix="/agent",
    tags=["AI Agent"],
)


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(request: ChatRequest):
    result = graph.invoke(
        {
            "message": request.message,
            "response": "",
        }
    )

    response = result["response"].strip()

    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    try:
        start = response.find("{")
        end = response.rfind("}")

        if start != -1 and end != -1:
            response = response[start:end + 1]

        return json.loads(response)

    except Exception as error:
        print("JSON parsing error:", error)
        print("Raw response:", response)

        return {
            "raw_response": response
        }