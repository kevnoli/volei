from sqlmodel import Field, Relationship, SQLModel


class TeamPlayer(SQLModel, table=True):
    order: int = Field(default=1)
    team_id: int = Field(foreign_key="team.id", primary_key=True)
    player_id: int = Field(foreign_key="player.id", primary_key=True)

    # Relationships
    team: "Team" = Relationship(back_populates="player_links")
    player: "Player" = Relationship()


from .team import Team
from .player import Player
