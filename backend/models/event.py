from datetime import datetime
from sqlmodel import Field, SQLModel, Relationship, Column, DateTime

from .event_player import EventPlayer


class EventBase(SQLModel):
    start_date: datetime = Field(
        sa_column=Column(
            DateTime(
                timezone=True),
            nullable=False))
    end_date: datetime = Field(
        sa_column=Column(
            DateTime(
                timezone=True),
            nullable=False))
    voting_until: datetime = Field(
        sa_column=Column(
            DateTime(
                timezone=True),
            nullable=False))
    checkin_from: datetime = Field(
        sa_column=Column(
            DateTime(
                timezone=True),
            nullable=False))
    checkin_until: datetime = Field(
        sa_column=Column(
            DateTime(
                timezone=True),
            nullable=False))


class Event(EventBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    # Relationships
    players: list["Player"] = Relationship(
        back_populates="events", link_model=EventPlayer)
    teams: list["Team"] = Relationship(
        back_populates="event")


class EventRead(EventBase):
    id: int
    players: list["PlayerRead"]
    teams: list["TeamRead"]


class EventCreate(EventBase):
    pass


class EventUpdate(EventBase):
    pass


from .player import Player, PlayerRead
from .team import Team, TeamRead
