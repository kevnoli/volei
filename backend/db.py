from sqlmodel import Session, create_engine
from os import getenv

engine = create_engine(getenv('DATABASE_URL'))


def get_session():
    with Session(engine) as session:
        yield session
