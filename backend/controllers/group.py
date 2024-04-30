from typing import List
from sqlmodel import Session, select
from fastapi import HTTPException

from models import Group, GroupRead, GroupCreate, GroupUpdate


def show(session: Session) -> List[GroupRead]:
    groups = session.exec(select(Group)).all()
    return groups


def index(group_id: int, session: Session) -> GroupRead:
    group = session.get(Group, group_id)
    if group:
        return group
    raise HTTPException(status_code=404, detail="Group not found")


def create(
        group_data: GroupCreate,
        session: Session) -> GroupRead:
    group = Group.model_validate(group_data)
    session.add(group)
    session.commit()
    session.refresh(group)
    return group


def remove(group_id: int, session: Session):
    group = session.get(Group, group_id)
    if group:
        session.delete(group)
        session.commit()
        return 204
    raise HTTPException(status_code=404, detail="Group not found")


def replace(group_id: int, group_data: GroupUpdate,
            session: Session) -> GroupRead:
    group = session.get(Group, group_id)
    if group:
        group_data = group_data.model_dump(exclude_unset=True)
        for key, value in group_data.items():
            setattr(group, key, value)
        session.add(group)
        session.commit()
        session.refresh(group)
        return group
    raise HTTPException(status_code=404, detail="Group not found")


def update(group_id: int, group_data: GroupUpdate,
           session: Session) -> GroupRead:

    pass
