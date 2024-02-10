#!/usr/bin/python3
'''
    Implementation of the State class
'''
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    '''
        Implementation for the State.
        Create relationship between class State (parent) to City (child)
    '''
    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initializes State"""
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        """Getter attribute for cities in case of file storage"""
        from models import storage
        cities_list = []
        for city in storage.all("City").values():
            if city.state_id == self.id:
                cities_list.append(city)
        return cities_list
