from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


engine = create_engine("postgresql+pg8000://postgres:21122008@localhost:5432/ep_tour", echo=True)
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass


def create_db():
    Base.metadata.create_all(bind=engine)