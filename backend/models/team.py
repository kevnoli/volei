from sqlmodel import Field, SQLModel, Relationship

from .team_player import TeamPlayer


class TeamBase(SQLModel):
    pass


class Team(TeamBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    event_id: int = Field(foreign_key="event.id")

    # Relationships
    event: "Event" = Relationship(back_populates="teams")
    players: list["Player"] = Relationship(link_model=TeamPlayer)


class TeamRead(TeamBase):
    id: int
    event_id: int
    players: list["PlayerRead"]


class TeamCreate(TeamBase):
    event_id: int
    players: list[int]


from .event import Event
from .player import Player, PlayerRead
