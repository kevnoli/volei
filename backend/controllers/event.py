from typing import List
from fastapi import HTTPException
from sqlmodel import Session, select
from models import Event, EventRead, EventCreate, EventUpdate


def show(session: Session) -> List[EventRead]:
    events = session.exec(select(Event)).all()
    return events


def index(event_id: int, session: Session) -> EventRead:
    event = session.get(Event, event_id)
    if not event:
        raise HTTPException(404, "Event not found.")
    return event


def create(
        event_data: EventCreate,
        session: Session) -> EventRead:
    event = Event.model_validate(event_data)
    session.add(event)
    session.commit()
    session.refresh(event)
    return event


def remove(event_id: int, session: Session):
    event = session.get(Event, event_id)
    if not event:
        raise HTTPException(404, "Event not found.")
    session.delete(event)
    session.commit()


def replace(event_id: int, event_data: EventUpdate,
            session: Session) -> EventRead:
    event = session.get(Event, event_id)
    if not event:
        raise HTTPException(404, "Event not found.")
    event_data = event_data.model_dump(exclude_unset=True)
    for key, value in event_data.items():
        setattr(event, key, value)
    session.add(event)
    session.commit()
    session.refresh(event)
    return event


def update(event_id: int, event_data: EventUpdate,
           session: Session) -> EventRead:

    pass
