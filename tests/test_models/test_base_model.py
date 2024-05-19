#!/usr/bin/python3
"""
Unit tests for the BaseModel class.

This module contains unit tests for the methods and attributes
of the BaseModel class from the models.base_model module.
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def test_initialization(self):
        """Test initialization of BaseModel instance"""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsNotNone(my_model.id)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)
        self.assertEqual(my_model.created_at, my_model.updated_at)

    def test_str_representation(self):
        """Test string representation of BaseModel instance"""
        my_model = BaseModel()
        expected_str = (
            f"[{my_model.__class__.__name__}] "
            f"({my_model.id}) "
            f"{my_model.__dict__}"
        )

        self.assertEqual(str(my_model), expected_str)

    def test_save_method(self):
        """Test save method of BaseModel"""
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method of BaseModel"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_dict = my_model.to_dict()
        expected_dict = {
            'id': my_model.id,
            'created_at': my_model.created_at.isoformat(),
            'updated_at': my_model.updated_at.isoformat(),
            'name': 'My First Model',
            'my_number': 89,
            '__class__': 'BaseModel'
        }
        self.assertDictEqual(my_model_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
