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
    Full_names = Column(String(50))
    Username = Column(String(15), unique=True)
    email = Column(String(50), unique=True)
    Password = Column(String(80))

engine = create_engine('sqlite:///Users.db')
Base.metadata.create_all(engine)