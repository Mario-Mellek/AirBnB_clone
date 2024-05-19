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
        """Test initialization of BaseModel"""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsNotNone(my_model.id)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)
        self.assertEqual(my_model.created_at, my_model.updated_at)

    def test_str_representation(self):
        """Test string representation of instance"""
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

    def test_initialization_with_kwargs(self):
        """Test initialization of BaseModel instance with kwargs added"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_dict = my_model.to_dict()
        new_model = BaseModel(**my_model_dict)
        self.assertEqual(new_model.id, my_model.id)
        self.assertEqual(new_model.created_at, my_model.created_at)
        self.assertEqual(new_model.updated_at, my_model.updated_at)
        self.assertEqual(new_model.name, my_model.name)
        self.assertEqual(new_model.my_number, my_model.my_number)

    def test_datetime_conversion(self):
        """Test datetime conversion for created_at and updated_at"""
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        new_model = BaseModel(**my_model_dict)
        self.assertIsInstance(new_model.created_at, datetime)
        self.assertIsInstance(new_model.updated_at, datetime)
        self.assertEqual(new_model.created_at, my_model.created_at)
        self.assertEqual(new_model.updated_at, my_model.updated_at)

    def test_to_dict_output_types(self):
        """Test to_dict method returns expected types"""
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict['id'], str)
        self.assertIsInstance(my_model_dict['created_at'], str)
        self.assertIsInstance(my_model_dict['updated_at'], str)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')

    def test_unique_id(self):
        """Test each BaseModel instance gets a unique id"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_save_updates_updated_at(self):
        """Test save method updates `updated_at` attribute"""
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        new_updated_at = my_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertGreater(new_updated_at, old_updated_at)


if __name__ == '__main__':
    unittest.main()
