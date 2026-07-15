from fastapi import APIRouter
from pydantic import BaseModel
import json

from app.graph.graph import graph

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
            "response": ""
        }
    )

    reply = result["response"]

    # Remove markdown if the model returns it
    reply = reply.replace("```json", "")
    reply = reply.replace("```", "")
    reply = reply.strip()

    try:
        return json.loads(reply)

    except Exception:

        return {
            "raw_response": reply
        }