#!/usr/bin/python3
"""Module for testing Review class"""
from tests.test_models.test_base_model import TestBaseModel
from models.review import Review


class TestReview(TestBaseModel):
    """Class to test the Review methods"""

    def __init__(self, *args, **kwargs):
        """Initialize the test case"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Test the place_id attribute of Review"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """Test the user_id attribute of Review"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Test the text attribute of Review"""
        new = self.value()
        self.assertEqual(type(new.text), str)


if __name__ == '__main__':
    unittest.main()
