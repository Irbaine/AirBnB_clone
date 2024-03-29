#!/usr/bin/python3
""" Place Module"""
from models.base_model import BaseModel


class Place(BaseModel):
    city_id = ""
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    name = ""
    description = ""
    number_rooms = 0
    user_id = ""
    number_bathrooms = 0
    max_guest = 0
