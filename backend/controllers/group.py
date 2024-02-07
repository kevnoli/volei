from typing import List
from fastapi import Depends
from sqlmodel import Session, select
from models import Group, GroupRead, GroupCreate, GroupUpdate
from db import get_session


def show(session: Session = Depends(get_session)) -> List[GroupRead]:
    groups = session.exec(select(Group)).all()
    return groups


def index(group_id: int, session: Session = Depends(get_session)) -> GroupRead:
    group = session.get(Group, group_id)
    return group


def create(
        group_data: GroupCreate,
        session: Session = Depends(get_session)) -> GroupRead:
    group = Group.model_validate(group_data)
    session.add(group)
    session.commit()
    session.refresh(group)
    return group


def remove(group_id: int, session: Session = Depends(get_session)):
    group = session.get(Group, group_id)
    if group:
        session.delete(group)
        session.commit()
    return 204


def replace(group_id: int, group_data: GroupUpdate,
            session: Session = Depends(get_session)) -> GroupRead:
    group = session.get(Group, group_id)
    if group:
        group_data = group_data.model_dump(exclude_unset=True)
        for key, value in group_data.items():
            setattr(group, key, value)
        session.add(group)
        session.commit()
        session.refresh(group)
    return group


def update(group_id: int, group_data: GroupUpdate,
           session: Session = Depends(get_session)) -> GroupRead:

    pass
