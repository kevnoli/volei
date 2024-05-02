from sqlmodel import Field, SQLModel
from datetime import time, timedelta


class ScheduleBase(SQLModel):
    weekday: int = Field(default=None, ge=0, le=6, nullable=False)
    start_date: time = Field(default=None, nullable=False)
    end_date: timedelta = Field(default=None, nullable=False)
    voting_until: timedelta = Field(default=None, nullable=False)
    checkin_from: timedelta = Field(default=None, nullable=False)
    checkin_until: timedelta = Field(default=None, nullable=False)


class Schedule (ScheduleBase, table=True):
    id: int = Field(default=None, primary_key=True)


class ScheduleRead(ScheduleBase):
    id: int


class ScheduleCreate(ScheduleBase):
    pass


class ScheduleUpdate(ScheduleBase):
    pass
