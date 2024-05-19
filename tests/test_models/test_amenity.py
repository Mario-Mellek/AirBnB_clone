#!/usr/bin/python3
"""
Unittest module for the Amenity class.
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def setUp(self):
        """Set up an Amenity instance for testing."""
        self.amenity = Amenity()

    def test_inheritance(self):
        """Test that Amenity is a subclass of BaseModel."""
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes(self):
        """Test that Amenity has the correct attributes."""
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")

    def test_to_dict(self):
        """Test the to_dict method."""
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertIsInstance(amenity_dict["created_at"], str)
        self.assertIsInstance(amenity_dict["updated_at"], str)

    def test_str(self):
        """Test the __str__ method."""
        amenity_str = str(self.amenity)
        self.assertIn("[Amenity]", amenity_str)
        self.assertIn("id", amenity_str)
        self.assertIn("created_at", amenity_str)
        self.assertIn("updated_at", amenity_str)

    def test_save(self):
        """Test the save method."""
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(self.amenity.updated_at, old_updated_at)


if __name__ == "__main__":
    unittest.main()
