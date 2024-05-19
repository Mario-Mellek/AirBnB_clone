#!/usr/bin/python3
"""
Unittest module for the Place class.
"""

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def setUp(self):
        """Set up a Place instance for testing."""
        self.place = Place()

    def test_inheritance(self):
        """Test that Place is a subclass of BaseModel."""
        self.assertIsInstance(self.place, BaseModel)

    def test_attributes(self):
        """Test that Place has the correct attributes."""
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertEqual(self.place.city_id, "")
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertEqual(self.place.user_id, "")
        self.assertTrue(hasattr(self.place, "name"))
        self.assertEqual(self.place.name, "")
        self.assertTrue(hasattr(self.place, "description"))
        self.assertEqual(self.place.description, "")
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertEqual(self.place.number_rooms, 0)
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertEqual(self.place.max_guest, 0)
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertEqual(self.place.price_by_night, 0)
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertEqual(self.place.latitude, 0.0)
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertEqual(self.place.longitude, 0.0)
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        self.assertEqual(self.place.amenity_ids, [])

    def test_to_dict(self):
        """Test the to_dict method."""
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertIsInstance(place_dict["created_at"], str)
        self.assertIsInstance(place_dict["updated_at"], str)

    def test_str(self):
        """Test the __str__ method."""
        place_str = str(self.place)
        self.assertIn("[Place]", place_str)
        self.assertIn("id", place_str)
        self.assertIn("created_at", place_str)
        self.assertIn("updated_at", place_str)

    def test_save(self):
        """Test the save method."""
        old_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(self.place.updated_at, old_updated_at)


if __name__ == "__main__":
    unittest.main()
