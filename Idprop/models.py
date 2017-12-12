from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

from . import settings

DeclarativeBase = declarative_base()


def db_connect():
    return create_engine(URL(**settings.DATABASE))


def create_deals_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class Person(DeclarativeBase):
    __tablename__ = "kitchen_bath_remodelers_idprop"

    name = Column('name', String, nullable=True)
    profile = Column('profile', String, nullable=True)
    email = Column('email', String, nullable=True)
    mobile = Column('mobile', String, nullable=True)
    url = Column('url', String, primary_key=True)
