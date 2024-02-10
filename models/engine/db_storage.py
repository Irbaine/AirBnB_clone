#!/usr/bin/python3
'''
    Define class DatabaseStorage
'''
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    '''
        Create SQLalchemy database
    '''
    __engine = None
    __session = None

    def __init__(self):
        '''
            Create engine and link to SQLite database
        '''
        # Use SQLite database URL format
        self.__engine = create_engine('sqlite:///AirBnB_Clone.db', echo=False)
        # Drop all tables if the environment is for testing
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''
            Query current database session
        '''
        db_dict = {}

        if cls is not None:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                db_dict[key] = obj
            return db_dict
        else:
            classes = [User, State, City, Place, Amenity, Review]
            for cls in classes:
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    db_dict[key] = obj
            return db_dict

    def new(self, obj):
        '''
            Add object to current database session
        '''
        self.__session.add(obj)

    def save(self):
        '''
            Commit all changes of current database session
        '''
        self.__session.commit()

    def delete(self, obj=None):
        '''
            Delete from current database session
        '''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        '''
            Create all tables in the database and session
        '''
        Base.metadata.create_all(self.__engine)
        session_factory = session(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        '''
            Remove private session attribute
        '''
        self.__session.close()
