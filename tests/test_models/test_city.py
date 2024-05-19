#!/usr/bin/python3
"""
Unittest module for the City class.
"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def setUp(self):
        """Set up a City instance for testing."""
        self.city = City()

    def test_inheritance(self):
        """Test that City is a subclass of BaseModel."""
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        """Test that City has the correct attributes."""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_to_dict(self):
        """Test the to_dict method."""
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict["__class__"], "City")
        self.assertIsInstance(city_dict["created_at"], str)
        self.assertIsInstance(city_dict["updated_at"], str)

    def test_str(self):
        """Test the __str__ method."""
        city_str = str(self.city)
        self.assertIn("[City]", city_str)
        self.assertIn("id", city_str)
        self.assertIn("created_at", city_str)
        self.assertIn("updated_at", city_str)

    def test_save(self):
        """Test the save method."""
        old_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(self.city.updated_at, old_updated_at)


if __name__ == "__main__":
    unittest.main()
