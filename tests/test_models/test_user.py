#!/usr/bin/python3
"""Module for testing User class"""
from tests.test_models.test_base_model import TestBaseModel
from models.user import User


class TestUser(TestBaseModel):
    """Class to test the User methods"""

    def __init__(self, *args, **kwargs):
        """Initialize the test case"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Test the first_name attribute of User"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Test the last_name attribute of User"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """Test the email attribute of User"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """Test the password attribute of User"""
        new = self.value()
        self.assertEqual(type(new.password), str)


if __name__ == '__main__':
    unittest.main()
