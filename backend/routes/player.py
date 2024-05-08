from fastapi import APIRouter
from fastapi import Depends
from sqlmodel import Session

from db import get_session

from models import PlayerRead, PlayerCreate, PlayerUpdate

from controllers import player

router = APIRouter(prefix='/players', tags=['players'])


@router.get('')
def fetch_players(session: Session = Depends(get_session)) -> list[PlayerRead]:
    return player.show(session)


@router.get('/{player_id}')
def fetch_player(
        player_id: int,
        session: Session = Depends(get_session)) -> PlayerRead:
    return player.index(player_id, session)


@router.post('', status_code=201)
def create_player(player_data: PlayerCreate,
                  session: Session = Depends(get_session)) -> PlayerRead:
    return player.create(player_data, session)


@router.delete('/{player_id}', status_code=204)
def remove_player(player_id: int, session: Session = Depends(get_session)):
    return player.remove(player_id, session)


@router.put('/{player_id}')
def replace_player(
        player_id: int,
        player_data: PlayerCreate,
        session: Session = Depends(get_session)) -> PlayerRead:
    return player.replace(player_id, player_data, session)


@router.patch('/{player_id}')
def update_player(player_id: int, player_data: PlayerUpdate,
                  session: Session = Depends(get_session)) -> PlayerRead:
    return player.update(player_id, player_data, session)
