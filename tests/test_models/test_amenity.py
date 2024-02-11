#!/usr/bin/python3
"""
This module contains the test suite for the Amenity class.
"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """
    Test cases for the Amenity class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the test case with the necessary attributes.
        """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """
        Test the type of the name attribute of the Amenity class.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
