#!/usr/bin/python3
"""Module for testing State class"""
from tests.test_models.test_base_model import TestBaseModel
from models.state import State


class TestState(TestBaseModel):
    """Class to test the State methods"""

    def __init__(self, *args, **kwargs):
        """Initialize the test case"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Test the name attribute of State"""
        new = self.value()
        self.assertEqual(type(new.name), str)


if __name__ == '__main__':
    unittest.main()
