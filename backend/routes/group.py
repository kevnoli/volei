from typing import List
from fastapi import APIRouter

from models import GroupRead, GroupCreate, GroupUpdate

from controllers import group

router = APIRouter(prefix='/groups', tags=['groups'])


@router.get('/')
def fetch_groups() -> List[GroupRead]:
    return group.show()


@router.get('/{group_id}')
def fetch_group(group_id: int) -> GroupRead:
    return group.index(group_id)


@router.post('', status_code=201)
def create_group(group_data: GroupCreate) -> GroupRead:
    return group.create(group_data)


@router.delete('/{group_id}', status_code=204)
def remove_group(group_id: int):
    return group.remove(group_id)


@router.put('/{group_id}')
def replace_group(group_id: int, group_data: GroupUpdate) -> GroupRead:
    return group.replace(group_id, group_data)


@router.patch('/{group_id}')
def update_group(group_id: int, group_data: GroupUpdate) -> GroupRead:
    return group.update(group_id, group_data)
