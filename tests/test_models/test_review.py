#!/usr/bin/python3
"""
Unittest module for the Review class.
"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def setUp(self):
        """Set up a Review instance for testing."""
        self.review = Review()

    def test_inheritance(self):
        """Test that Review is a subclass of BaseModel."""
        self.assertIsInstance(self.review, BaseModel)

    def test_attributes(self):
        """Test that Review has the correct attributes."""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertEqual(self.review.place_id, "")
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertEqual(self.review.user_id, "")
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(self.review.text, "")

    def test_to_dict(self):
        """Test the to_dict method."""
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertIsInstance(review_dict["created_at"], str)
        self.assertIsInstance(review_dict["updated_at"], str)

    def test_str(self):
        """Test the __str__ method."""
        review_str = str(self.review)
        self.assertIn("[Review]", review_str)
        self.assertIn("id", review_str)
        self.assertIn("created_at", review_str)
        self.assertIn("updated_at", review_str)

    def test_save(self):
        """Test the save method."""
        old_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(self.review.updated_at, old_updated_at)


if __name__ == "__main__":
    unittest.main()
