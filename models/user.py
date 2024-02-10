#!/usr/bin/python3
"""Class User"""
from models.base_model import BaseModel


class User(BaseModel):
    first_name = ''
    last_name = ''
    email = ''
    password = ''
