from sqlmodel import Field, SQLModel, Relationship


class TeamBase(SQLModel):
    pass


class Team(TeamBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    event_id: int = Field(foreign_key="event.id")

    # Relationships
    event: "Event" = Relationship(back_populates="teams")
    player_links: list["TeamPlayer"] = Relationship(back_populates="team")


class TeamRead(TeamBase):
    id: int
    event_id: int
    players: list["TeamPlayer"]


class TeamCreate(TeamBase):
    event_id: int
    players: list[int]


from .event import Event
from .team_player import TeamPlayer
