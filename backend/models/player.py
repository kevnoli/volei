from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional
from models import GroupPlayer, EventPlayer

class Player(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    # Relationships
    group_association: List["GroupPlayer"] = Relationship(back_populates="player")
    event_association: List["EventPlayer"] = Relationship(back_populates="player")