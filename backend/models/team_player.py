from sqlmodel import Field, SQLModel


class TeamPlayer(SQLModel, table=True):
    order: int = Field(default=1)
    team_id: int = Field(foreign_key="team.id", primary_key=True)
    player_id: int = Field(foreign_key="player.id", primary_key=True)
