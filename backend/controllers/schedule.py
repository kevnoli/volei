from typing import List
from fastapi import HTTPException
from sqlmodel import Session, select

from models import Schedule, ScheduleRead, ScheduleCreate, ScheduleUpdate


def show(session: Session) -> List[ScheduleRead]:
    schedule = session.exec(select(Schedule)).all()

    return schedule


def create(
        schedule_data: ScheduleCreate,
        session: Session) -> ScheduleRead:
    schedule = Schedule.model_validate(schedule_data)
    session.add(schedule)
    session.commit()
    session.refresh(schedule)
    return schedule


def remove(schedule_id: int, session: Session):
    schedule = session.get(Schedule, schedule_id)
    if schedule:
        session.delete(schedule)
        session.commit()
        return 204
    raise HTTPException(status_code=404, detail="Schedule not found")


def replace(schedule_id: int, schedule_data: Schedule,
            session: Session) -> ScheduleRead:
    schedule = session.get(Schedule, schedule_id)
    if schedule:
        schedule_data = schedule_data.model_dump(exclude_unset=True)
        for key, value in schedule_data.items():
            setattr(schedule, key, value)
        session.add(schedule)
        session.commit()
        session.refresh(schedule)
        return schedule
    raise HTTPException(status_code=404, detail="Schedule not found")


def update(schedule_id: int, schedule_data: ScheduleUpdate,
           session: Session) -> ScheduleRead:

    pass
