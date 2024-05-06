from decimal import Decimal
from sqlmodel import Field, SQLModel, Relationship

from .event_player import EventPlayer


class PlayerBase(SQLModel):
    first_name: str
    last_name: str
    overall_rating: Decimal = Field(default=0, max_digits=3, decimal_places=2)
    admin: bool = Field(default=False)


class Player(PlayerBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    # Relationships
    events: list["Event"] = Relationship(
        back_populates="players", link_model=EventPlayer)


class PlayerRead(PlayerBase):
    id: int


class PlayerCreate(PlayerBase):
    pass


class PlayerUpdate(PlayerBase):
    first_name: str | None
    last_name: str | None
    overall_rating: Decimal | None


from .event import Event
