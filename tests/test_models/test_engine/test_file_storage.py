#!/usr/bin/python3
"""Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """Class to test the file storage methods"""

    def setUp(self):
        """Set up test environment"""
        # Delete all objects from the storage
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Remove storage file at end of tests"""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_objects_is_empty(self):
        """__objects is initially empty"""
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """New object is correctly added to __objects"""
        new_model = BaseModel()
        self.assertIn('BaseModel.' + new_model.id, storage.all().keys())

    def test_all(self):
        """__objects is properly returned"""
        new_model = BaseModel()
        self.assertIsInstance(storage.all(), dict)

    def test_base_model_instantiation(self):
        """File is not created on BaseModel save"""
        new_model = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_save(self):
        """FileStorage save method"""
        new_model = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """Storage file is successfully loaded to __objects"""
        new_model = BaseModel()
        storage.save()
        storage.reload()
        self.assertIn('BaseModel.' + new_model.id, storage.all().keys())

    def test_reload_empty(self):
        """Load from an empty file"""
        with open('file.json', 'w') as file:
            file.write('')
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """Nothing happens if file does not exist"""
        self.assertIsNone(storage.reload())

    def test_base_model_save(self):
        """BaseModel save method calls storage save"""
        new_model = BaseModel()
        new_model.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """Confirm __file_path is string"""
        self.assertIsInstance(storage._FileStorage__file_path, str)

    def test_type_objects(self):
        """Confirm __objects is a dict"""
        self.assertIsInstance(storage.all(), dict)

    def test_key_format(self):
        """Key is properly formatted"""
        new_model = BaseModel()
        key = 'BaseModel.' + new_model.id
        self.assertIn(key, storage.all().keys())

    def test_storage_var_created(self):
        """FileStorage object storage created"""
        self.assertIsInstance(storage, FileStorage)


if __name__ == '__main__':
    unittest.main()
