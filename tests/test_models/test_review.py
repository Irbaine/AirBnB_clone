#!/usr/bin/python3
"""test for review"""
import unittest
import os
from models.review import Review
from models.base_model import BaseModel
import pep8
from os import getenv


class TestReview(unittest.TestCase):
    """this will test the review class"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.review = Review()
        cls.review.place_id = "2005-winners"
        cls.review.user_id = "1937-wydad"
        cls.review.text = "The jokes on you"

    @classmethod
    def tearDownClass(cls):
        """at the end of the test this will tear it down"""
        del cls.review

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Review(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_Review(self):
        """checking for docstrings"""
        self.assertIsNotNone(Review.__doc__)

    def test_attributes_Review(self):
        """checking if Review has attributes"""
        self.assertTrue('id' in self.review.__dict__)
        self.assertTrue('created_at' in self.review.__dict__)
        self.assertTrue('updated_at' in self.review.__dict__)
        self.assertTrue('place_id' in self.review.__dict__)
        self.assertTrue('user_id' in self.review.__dict__)
        self.assertTrue('text' in self.review.__dict__)

    def test_is_subclass_Review(self):
        """test if Review is subclass of BaseModel"""
        self.assertTrue(issubclass(self.review.__class__, BaseModel), True)

    def test_attribute_types_Review(self):
        """test attribute type for Review"""
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.user_id), str)
        self.assertEqual(type(self.review.text), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', "can't")
    def test_save_Review(self):
        """test if the save works"""
        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)

    def test_to_dict_Review(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.review), True)


if __name__ == "__main__":
    unittest.main()
