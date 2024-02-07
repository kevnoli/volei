from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional
from .event import Event


class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    event_id: int = Field(foreign_key="event.id")
    name: str

    # Relationships
    event: "Event" = Relationship(back_populates="teams")
    players: List["TeamPlayer"] = Relationship(back_populates="team")


from .team_player import TeamPlayer
