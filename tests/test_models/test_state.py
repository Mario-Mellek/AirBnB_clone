#!/usr/bin/python3
"""
Unittest module for the State class.
"""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def setUp(self):
        """Set up a State instance for testing."""
        self.state = State()

    def test_inheritance(self):
        """Test that State is a subclass of BaseModel."""
        self.assertIsInstance(self.state, BaseModel)

    def test_attributes(self):
        """Test that State has the correct attributes."""
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")

    def test_to_dict(self):
        """Test the to_dict method."""
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict["__class__"], "State")
        self.assertIsInstance(state_dict["created_at"], str)
        self.assertIsInstance(state_dict["updated_at"], str)

    def test_str(self):
        """Test the __str__ method."""
        state_str = str(self.state)
        self.assertIn("[State]", state_str)
        self.assertIn("id", state_str)
        self.assertIn("created_at", state_str)
        self.assertIn("updated_at", state_str)

    def test_save(self):
        """Test the save method."""
        old_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(self.state.updated_at, old_updated_at)


if __name__ == "__main__":
    unittest.main()
