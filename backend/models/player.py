from decimal import Decimal
from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional


class PlayerBase(SQLModel):
    first_name: str
    last_name: str
    overall_rating: Decimal = Field(default=0, max_digits=3, decimal_places=2)


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
