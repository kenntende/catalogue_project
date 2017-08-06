#configuration code
import os
import sys
import sqlite3

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Users(Base): #class definition

    __tablename__='Users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Full_names = Column(String(50), nullable=False)
    Username = Column(String(15), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    Password = Column(String(80), nullable=False)

engine = create_engine('sqlite:///Users.db')
Base.metadata.create_all(engine)