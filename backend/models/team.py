from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional
from .event import Event
from .player import PlayerRead


class TeamBase(SQLModel):
    pass


class Team(TeamBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    event_id: int = Field(foreign_key="event.id")

    # Relationships
    event: "Event" = Relationship(back_populates="teams")
    players: List["TeamPlayer"] = Relationship(back_populates="team")


class TeamRead(TeamBase):
    id: int
    event_id: int
    players: List["PlayerRead"]


class TeamCreate(TeamBase):
    event_id: int
    players: List[int]


from .team_player import TeamPlayer
