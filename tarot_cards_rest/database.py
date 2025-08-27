from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tarot_cards_rest.models import Base

engine = create_engine("sqlite:///db.sqlite3", echo=True)
Session = sessionmaker(engine, expire_on_commit=False)


def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()


if __name__ == "__main__":
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
