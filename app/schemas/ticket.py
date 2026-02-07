from typing import Optional
from pydantic import BaseModel, Field

class TicketCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str = ""

class TicketUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    description: Optional[str] = None
    status: Optional[str] = Field(default=None, pattern="^(open|in_progress|closed)$")

class TicketOut(BaseModel):
    id: int
    title: str
    description: str
    status: str

    class Config:
        from_attributes = True