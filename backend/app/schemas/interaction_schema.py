from datetime import date, time
from typing import Optional

from pydantic import BaseModel


class InteractionCreate(BaseModel):
    hcp_name: str
    interaction_type: str
    interaction_date: Optional[date] = None
    interaction_time: Optional[time] = None
    attendees: str
    topics_discussed: str
    materials_shared: str
    samples_distributed: str
    sentiment: str
    outcomes: str
    follow_up: str


class InteractionResponse(InteractionCreate):
    id: int

    class Config:
        from_attributes = True