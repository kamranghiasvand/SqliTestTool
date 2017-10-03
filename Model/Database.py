import os
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


BASE = declarative_base()
DB_NAME = 'database.db'
DB_PATH = os.path.dirname(os.path.realpath(__file__))
ENGINE = create_engine('sqlite://')


def init(dbname, dbpath):
    if type(dbname) is String and dbname:
        DB_NAME = dbname
    if os.path.isdir(dbpath):
        DB_PATH = dbpath
    ENGINE = create_engine('sqlite:///' + DB_PATH + DB_NAME)
    session = sessionmaker()
    session.configure(bind=ENGINE)
    BASE.metadata.create_all(ENGINE)
