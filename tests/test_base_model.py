import unittest
from AirBnB_clone.models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """The class for my test case"""
    def setUp(self):
        BaseModel()

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
