from typing import List
from fastapi import APIRouter

from models import EventRead, EventCreate, EventUpdate

from controllers import event

router = APIRouter(prefix='/events', tags=['events'])


@router.get('/')
def fetch_events() -> List[EventRead]:
    return event.show()


@router.get('/{event_id}')
def fetch_event(event_id: int) -> EventRead:
    return event.index(event_id)


@router.post('', status_code=201)
def create_event(event_data: EventCreate) -> EventRead:
    return event.create(event_data)


@router.delete('/{event_id}', status_code=204)
def remove_event(event_id: int):
    return event.remove(event_id)


@router.put('/{event_id}')
def replace_event(event_id: int, event_data: EventUpdate) -> EventRead:
    return event.replace(event_id, event_data)


@router.patch('/{event_id}')
def update_event(event_id: int, event_data: EventUpdate) -> EventRead:
    return event.update(event_id, event_data)
