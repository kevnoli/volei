from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional


class Group(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    # Relationships
    events: List["Event"] = Relationship(back_populates="group")
    players: List["GroupPlayer"] = Relationship(back_populates="group")

    
from .event import Event
from .group_player import GroupPlayer