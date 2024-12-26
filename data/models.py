from typing import List

from sqlalchemy import String, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask_login import UserMixin

from data.base import Base


class Tour(Base):
    __tablename__ = "tours"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(80))
    description: Mapped[str] = mapped_column(String(200))
    departure: Mapped[str] = mapped_column(String(30))
    picture: Mapped[str] = mapped_column(String(1000))
    price: Mapped[int] = mapped_column()
    stars: Mapped[str] = mapped_column(String(20))
    country: Mapped[str] = mapped_column(String(69))
    nights: Mapped[str] = mapped_column(String(25))
    date: Mapped[str] = mapped_column(String(42))

tour_user_asc = Table(
    "tour_user_asc",
    Base.metadata,
    Column("tour_id", ForeignKey("tours.id"), primary_key=True),
    Column("user_id", ForeignKey("users.id"), primary_key=True)
)

class User(Base, UserMixin):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(100), unique=True)
    email: Mapped[str] = mapped_column(String(599), unique=True)
    password: Mapped[str] = mapped_column(String(599))
    tours: Mapped[List[Tour]] = relationship(secondary=tour_user_asc)