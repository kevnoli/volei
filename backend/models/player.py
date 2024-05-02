from decimal import Decimal
from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional


class PlayerBase(SQLModel):
    first_name: str
    last_name: str
    overall_rating: Decimal = Field(default=0, max_digits=3, decimal_places=2)
    admin: bool = Field(default=False)


class Player(PlayerBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    # Relationships
    event_association: List["EventPlayer"] = Relationship(
        back_populates="player")


class PlayerRead(PlayerBase):
    id: int


class PlayerCreate(PlayerBase):
    pass


class PlayerUpdate(PlayerBase):
    first_name: Optional[str]
    last_name: Optional[str]
    overall_rating: Optional[Decimal]


from .event_player import EventPlayer
