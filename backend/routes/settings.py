from fastapi import APIRouter, Depends
from sqlmodel import Session

from models import ScheduleRead, ScheduleCreate, ScheduleUpdate
from db import get_session
from controllers import schedule


def is_admin():
    pass


router = APIRouter(
    prefix='/settings',
    tags=['settings'],
    dependencies=[
        Depends(is_admin)])


@router.get('/schedule')
def fetch_schedule(session: Session = Depends(
        get_session)) -> list[ScheduleRead]:
    return schedule.show(session)


@router.post('/schedule', status_code=201)
def create_schedule(schedule_data: ScheduleCreate,
                    session: Session = Depends(get_session)) -> ScheduleRead:
    return schedule.create(schedule_data, session)


@router.delete('/schedule/{schedule_id}', status_code=204)
def remove_schedule(schedule_id: int, session: Session = Depends(get_session)):
    return schedule.remove(schedule_id, session)


@router.put('/schedule/{schedule_id}')
def replace_schedule(
        schedule_id: int,
        schedule_data: ScheduleCreate,
        session: Session = Depends(get_session)) -> ScheduleRead:
    return schedule.replace(schedule_id, schedule_data, session)


@router.patch('/schedule/{schedule_id}')
def update_schedule(schedule_id: int, schedule_data: ScheduleUpdate,
                    session: Session = Depends(get_session)) -> ScheduleRead:
    return schedule.update(schedule_id, schedule_data, session)
