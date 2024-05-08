from sqlmodel import Field, Relationship, SQLModel


class TeamPlayer(SQLModel, table=True):
    team_id: int = Field(foreign_key="team.id", primary_key=True)
    player_id: int = Field(foreign_key="player.id", primary_key=True)
