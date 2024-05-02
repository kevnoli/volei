from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session
from db import get_session

from models import GroupRead, GroupCreate, GroupUpdate, EventRead

from controllers import group, event

router = APIRouter(prefix='/groups', tags=['groups'])


@router.get('')
def fetch_groups(session: Session = Depends(get_session)) -> List[GroupRead]:
    return group.show(session)


@router.get('/{group_id}')
def fetch_group(
        group_id: int,
        session: Session = Depends(get_session)) -> GroupRead:
    return group.index(group_id, session)


@router.post('', status_code=201)
def create_group(
        group_data: GroupCreate,
        session: Session = Depends(get_session)) -> GroupRead:
    return group.create(group_data, session)


@router.delete('/{group_id}', status_code=204)
def remove_group(group_id: int, session: Session = Depends(get_session)):
    return group.remove(group_id, session)


@router.put('/{group_id}')
def replace_group(group_id: int, group_data: GroupUpdate,
                  session: Session = Depends(get_session)) -> GroupRead:
    return group.replace(group_id, group_data, session)


@router.patch('/{group_id}')
def update_group(group_id: int, group_data: GroupUpdate,
                 session: Session = Depends(get_session)) -> GroupRead:
    return group.update(group_id, group_data, session)


@router.get('/{group_id}/events')
def fetch_all_events(
        group_id: int,
        session: Session = Depends(get_session)) -> List[EventRead]:
    return event.show_from_group(group_id, session)
