from sqlmodel import Field, SQLModel


class EventPlayer(SQLModel, table=True):
    event_id: int | None = Field(
        default=None,
        foreign_key="event.id",
        primary_key=True)
    player_id: int | None = Field(
        default=None,
        foreign_key="player.id",
        primary_key=True)
