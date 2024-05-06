from sqlmodel import Field, SQLModel, Relationship


class EventPlayer(SQLModel, table=True):
    event_id: int = Field(foreign_key="event.id", primary_key=True)
    player_id: int = Field(foreign_key="player.id", primary_key=True)

    # Relationships
    event: "Event" = Relationship(back_populates="players")
    player: "Player" = Relationship(back_populates="events")


from .event import Event
from .player import Player
