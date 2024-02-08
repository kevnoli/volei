from typing import List
from sqlmodel import Session, select
from models import Event, EventRead, EventCreate, EventUpdate


def show(session: Session) -> List[EventRead]:
    events = session.exec(select(Event)).all()
    return events


def index(event_id: int, session: Session) -> EventRead:
    event = session.get(Event, event_id)
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
    if event:
        session.delete(event)
        session.commit()
    return 204


def replace(event_id: int, event_data: EventUpdate,
            session: Session) -> EventRead:
    event = session.get(Event, event_id)
    if event:
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
