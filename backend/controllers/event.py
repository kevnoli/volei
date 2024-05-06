from fastapi import HTTPException
from sqlmodel import Session, select
from models import Event, EventRead, EventCreate, EventUpdate, Team, TeamPlayer
from random import shuffle


def show(session: Session) -> list[EventRead]:
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


def show_teams(event_id: int, session: Session):
    event = session.get(Event, event_id)

    return event.teams


def create_teams(event_id: int, teams: int, session: Session):
    event = session.get(Event, event_id)

    players = [player for player in event.players]
    shuffle(players)

    team_list = [{"team": Team(order=i, event=event_id), "rating": 0}
                 for i in range(teams)]

    session.add_all([team["team"] for team in team_list])

    def calculate_ratings():
        for team in team_list:
            team["rating"] = sum(
                [player.rating for player in players if player.team == team.team])

    def get_lowest_rated_team() -> Team:
        lowest_rated_team = None
        lowest_rating = 5
        for team in team_list:
            if team["rating"] < lowest_rating:
                lowest_rating = team["rating"]
                lowest_rated_team = team["team"]
        return lowest_rated_team

    for player in players:
        calculate_ratings()
        team = get_lowest_rated_team()
        player_link = TeamPlayer(player=player, team=team)
        session.add(player_link)

    session.commit()
    session.refresh(event)
    return event.teams
