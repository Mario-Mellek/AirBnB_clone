#!/usr/bin/python3
"""
Unittest module for the User class.
"""

import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def setUp(self):
        """Set up a User instance for testing."""
        self.user = User()

    def test_inheritance(self):
        """Test that User is a subclass of BaseModel."""
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        """Test that User has the correct attributes."""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_to_dict(self):
        """Test the to_dict method."""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict["__class__"], "User")
        self.assertIsInstance(user_dict["created_at"], str)
        self.assertIsInstance(user_dict["updated_at"], str)

    def test_str(self):
        """Test the __str__ method."""
        user_str = str(self.user)
        self.assertIn("[User]", user_str)
        self.assertIn("id", user_str)
        self.assertIn("created_at", user_str)
        self.assertIn("updated_at", user_str)

    def test_save(self):
        """Test the save method."""
        old_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(self.user.updated_at, old_updated_at)


if __name__ == "__main__":
    unittest.main()
