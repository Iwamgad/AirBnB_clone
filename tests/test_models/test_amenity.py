#!/usr/bin/python3

"""This module tests the Amenity class"""

from models.amenity import Amenity
import unittest


class TestAmenity_instantiation(unittest.TestCase):
    """A test class for the Amenity class"""

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_name_is_public_class_attribute(self):
        am = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
if __name__ == "__main__":
    unittest.main()
