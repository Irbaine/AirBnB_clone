#!/usr/bin/python3
"""Module for testing Place class"""
from tests.test_models.test_base_model import TestBaseModel
from models.place import Place


class TestPlace(TestBaseModel):
    """Class to test the Place methods"""

    def __init__(self, *args, **kwargs):
        """Initialize the test case"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Test the city_id attribute of Place"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """Test the user_id attribute of Place"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """Test the name attribute of Place"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """Test the description attribute of Place"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """Test the number_rooms attribute of Place"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """Test the number_bathrooms attribute of Place"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """Test the max_guest attribute of Place"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """Test the price_by_night attribute of Place"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """Test the latitude attribute of Place"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """Test the longitude attribute of Place"""
        new = self.value()
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """Test the amenity_ids attribute of Place"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)


if __name__ == '__main__':
    unittest.main()
