from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional


class PlayerBase(SQLModel):
    name: str


class Player(PlayerBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    # Relationships
    group_association: List["GroupPlayer"] = Relationship(
        back_populates="player")
    event_association: List["EventPlayer"] = Relationship(
        back_populates="player")


class PlayerRead(PlayerBase):
    id: int


class PlayerCreate(PlayerBase):
    pass


class PlayerUpdate(PlayerBase):
    pass


from .group_player import GroupPlayer
from .event_player import EventPlayer
