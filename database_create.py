#configuration code
import os
import sys



from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class movie_collection(Base): #class definition
    __tablename__ = 'Movies'
    id = Column(Integer, primary_key=True, autoincrement=True)
    movie_title = Column(String(50), nullable=False)
    genre = Column(String(15))
    Story_line = Column(String(''))

class novel_collection(Base):
    __tablename__ = 'Novels'
    id = Column(Integer, primary_key=True, autoincrement=True)
    novel_title = Column(String(50), nullable=False)
    genre = Column(String(15))
    plot = Column(String(''))

class tv_series(Base):
    __tablename__ = 'tv_series'
    id = Column(Integer, primary_key=True, autoincrement=True)
    series_title = Column(String(50), nullable=False)
    genre = Column(String(15))
    storyline = Column(String(''))

class tv_shows(Base):
    __tablename__ = 'tv_shows'
    id = Column(Integer, primary_key=True, autoincrement=True)
    show_title = Column(String(50), nullable=False)
    genre = Column(String(15))


engine = create_engine('sqlite:///Collection.db')
Base.metadata.create_all(engine)