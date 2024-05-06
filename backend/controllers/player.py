from fastapi import HTTPException
from sqlmodel import Session, select
from models import Player, PlayerRead, PlayerCreate, PlayerUpdate


def show(session: Session) -> list[PlayerRead]:
    players = session.exec(select(Player)).all()
    return players


def index(player_id: int, session: Session) -> PlayerRead:
    player = session.get(Player, player_id)
    if player:
        return player
    raise HTTPException(status_code=404, detail="Player not found")


def create(
        player_data: PlayerCreate,
        session: Session) -> PlayerRead:
    player = Player.model_validate(player_data)
    session.add(player)
    session.commit()
    session.refresh(player)
    return player


def remove(player_id: int, session: Session):
    player = session.get(Player, player_id)
    if player:
        session.delete(player)
        session.commit()
        return 204
    raise HTTPException(status_code=404, detail="Player not found")


def replace(player_id: int, player_data: PlayerUpdate,
            session: Session) -> PlayerRead:
    player = session.get(Player, player_id)
    if player:
        player_data = player_data.model_dump(exclude_unset=True)
        for key, value in player_data.items():
            setattr(player, key, value)
        session.add(player)
        session.commit()
        session.refresh(player)
        return player
    raise HTTPException(status_code=404, detail="Player not found")


def update(player_id: int, player_data: PlayerUpdate,
           session: Session) -> PlayerRead:

    pass
