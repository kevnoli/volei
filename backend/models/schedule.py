from sqlmodel import Field, SQLModel
from datetime import time


class Schedule (SQLModel):
    weekday: int = Field(default=None, ge=0, le=6, nullable=False)
    start_date: time = Field(default=None, nullable=False)
    end_date: time = Field(default=None, nullable=False)
    voting_until: time = Field(default=None, nullable=False)
    checkin_from: time = Field(default=None, nullable=False)
    checkin_until: time = Field(default=None, nullable=False)
