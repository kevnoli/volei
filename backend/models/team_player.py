from sqlmodel import Field, SQLModel, Relationship
from .team import Team
from .player import Player


class TeamPlayer(SQLModel, table=True):
    team_id: int = Field(foreign_key="team.id", primary_key=True)
    player_id: int = Field(foreign_key="player.id", primary_key=True)
    # Relationships

    team: Team = Relationship(back_populates="players")
    player: Player = Relationship()
