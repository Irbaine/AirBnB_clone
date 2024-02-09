#!/usr/bin/python3
'''
    Implementation of the Review class
'''
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    '''
        Implementation for the Review.
    '''
    __tablename__ = "reviews"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """Initializes Review"""
        super().__init__(*args, **kwargs)

    @property
    def place(self):
        """Getter attribute for place in case of file storage"""
        from models import storage
        place = storage.get("Place", self.place_id)
        return place

    @property
    def user(self):
        """Getter attribute for user in case of file storage"""
        from models import storage
        user = storage.get("User", self.user_id)
        return user
