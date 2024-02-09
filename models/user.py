#!/usr/bin/python3
'''
    Implementation of the User class which inherits from BaseModel
'''
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    '''
        Definition of the User class
    '''
    __tablename__ = "users"
    if getenv("HBNB_TYPE_STORAGE", "fs") == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user",
                              cascade="all, delete, delete-orphan")
        reviews = relationship("Review", backref="user",
                               cascade="all, delete, delete-orphan")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes User"""
        super().__init__(*args, **kwargs)

    @property
    def places(self):
        """Getter attribute for places in case of file storage"""
        from models import storage
        places_list = []
        for place in storage.all("Place").values():
            if place.user_id == self.id:
                places_list.append(place)
        return places_list

    @property
    def reviews(self):
        """Getter attribute for reviews in case of file storage"""
        from models import storage
        reviews_list = []
        for review in storage.all("Review").values():
            if review.user_id == self.id:
                reviews_list.append(review)
        return reviews_list
