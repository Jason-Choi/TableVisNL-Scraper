from sqlalchemy import create_engine, Column, Table, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, String, Date, DateTime, Float, Boolean, Text)
from scrapy.utils.project import get_project_settings

Base = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"), encoding="utf-8")


def create_table(engine):
    Base.metadata.create_all(engine)


class Statista(Base):
    __tablename__ = "statista"
    
    id = Column(Integer, primary_key=True, unique=True)
    title = Column(Text)
    market = Column(Text)
    topic = Column(Text)
    spec = Column(Text)
    caption = Column(Text)

    