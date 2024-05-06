from fastapi import APIRouter, Depends
from sqlmodel import Session
from db import get_session

from models import EventRead, EventCreate, EventUpdate

from controllers import event

router = APIRouter(prefix='/events', tags=['events'])


@router.get('')
def fetch_events(session: Session = Depends(get_session)) -> list[EventRead]:
    return event.show(session)


@router.get('/{event_id}')
def fetch_event(
        event_id: int,
        session: Session = Depends(get_session)) -> EventRead:
    return event.index(event_id, session)


@router.post('', status_code=201)
def create_event(
        event_data: EventCreate,
        session: Session = Depends(get_session)) -> EventRead:
    return event.create(event_data, session)


@router.delete('/{event_id}', status_code=204)
def remove_event(event_id: int, session: Session = Depends(get_session)):
    return event.remove(event_id, session)


@router.put('/{event_id}')
def replace_event(event_id: int, event_data: EventUpdate,
                  session: Session = Depends(get_session)) -> EventRead:
    return event.replace(event_id, event_data, session)


@router.patch('/{event_id}')
def update_event(event_id: int, event_data: EventUpdate,
                 session: Session = Depends(get_session)) -> EventRead:
    return event.update(event_id, event_data, session)


@router.get('/{event_id}/teams')
def fetch_event_teams(event_id: int, session: Session = Depends(get_session)):
    return event.show_teams(event_id, session)


@router.post('/{event_id}/teams')
def create_event_teams(
        event_id: int,
        teams: int,
        session: Session = Depends(get_session)):
    return event.create_teams(event_id, teams, session)
