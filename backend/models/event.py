from datetime import datetime
from sqlmodel import Field, SQLModel, Relationship, Column, DateTime
from typing import List, Optional


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
    id: Optional[int] = Field(default=None, primary_key=True)

    # Relationships
    teams: List["Team"] = Relationship(back_populates="event")
    players: List["EventPlayer"] = Relationship(back_populates="event")


class EventRead(EventBase):
    id: int
    teams: List["Team"]
    players: List["EventPlayer"]


class EventCreate(EventBase):
    pass


class EventUpdate(EventBase):
    pass


from .team import Team
from .event_player import EventPlayer
