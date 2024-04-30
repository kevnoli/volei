from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional


class GroupBase(SQLModel):
    name: str


class Group(GroupBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    # Relationships
    events: List["Event"] = Relationship(back_populates="group")
    players: List["GroupPlayer"] = Relationship(back_populates="group")


class GroupRead(GroupBase):
    id: int
    players: List["GroupPlayer"]


class GroupCreate(GroupBase):
    pass


class GroupUpdate(GroupBase):
    pass


from .group_player import GroupPlayer
from .event import Event
