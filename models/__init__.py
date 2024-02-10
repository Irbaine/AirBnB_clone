#!/usr/bin/python3
'''
    Package initializer for the AirBnB clone project.
'''
from os import getenv
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

# Determine the storage type based on the environment variable
# If the variable is set to "db", use the database storage engine
# Otherwise, use the file storage engine
if getenv("HBNB_TYPE_STORAGE", "fs") == "db":
    from models.engine import db_storage
    storage = db_storage.DBStorage()
else:
    from models.engine import file_storage
    storage = file_storage.FileStorage()

# Dictionary to map class names to their respective classes
classes = {
    "User": User,
    "BaseModel": BaseModel,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review
}

# Reload the storage engine to load any existing data
storage.reload()

# Function to retrieve a class based on its name


def get_class(class_name):
    """
    Retrieve a class based on its name.
    Args:
    class_name(str): The name of the class to retrieve.
    Returns:
    The class if it exists, otherwise None.
    """
    return classes.get(class_name)
