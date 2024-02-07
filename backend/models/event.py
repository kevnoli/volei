from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional
from models import Group, Team, EventPlayer

class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    group_id: int = Field(foreign_key="group.id")
    name: str
    
    # Relationships
    group: Group = Relationship(back_populates="events")
    teams: List["Team"] = Relationship(back_populates="event")
    players: List["EventPlayer"] = Relationship(back_populates="event")
