#!/usr/bin/python3
'''
    Implementation of the Amenity class
'''
from os import getenv
from models.base_model import BaseModel, Base
from models.place import place_amenity
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    '''
        Implementation for the Amenities.
    '''
    __tablename__ = "amenities"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity,
                                       back_populates="amenities")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initializes Amenity"""
        super().__init__(*args, **kwargs)

    @property
    def places(self):
        """Getter attribute in case of file storage"""
        from models import storage
        place_list = []
        for place in storage.all("Place").values():
            if self.id in place.amenity_ids:
                place_list.append(place)
        return place_list
