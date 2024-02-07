from sqlmodel import Field, SQLModel, Relationship
from .group import Group
from .player import Player

class GroupPlayer(SQLModel, table=True):
    group_id: int = Field(foreign_key="group.id", primary_key=True)
    player_id: int = Field(foreign_key="player.id", primary_key=True)
    is_admin: bool = Field(default=False)

    # Relationships
    group: Group = Relationship(back_populates="players")
    player: Player = Relationship(back_populates="group_association")