#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """The class for my test case"""
    def setUp(self):
        """initializes a scenario"""
        self.model = BaseModel()

    def test_str_method(self):
        """Makes sure the string output is correct"""


if __name__ == '__main__':
    unittest.main()
