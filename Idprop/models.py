from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

from . import settings

DeclarativeBase = declarative_base()


def db_connect():
    return create_engine(URL(**settings.DATABASE))


def create_deals_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class Person(DeclarativeBase):
    __tablename__ = "architects_idprop"

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    profile = Column('profile', String, nullable=True)
    email = Column('email', String, nullable=True)
    mobile = Column('mobile', String, nullable=True)
    url = Column('url', String, nullable=True)
