#!/usr/bin/python3
""" Review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    user_id = ""
    text = ""
    place_id = ""
