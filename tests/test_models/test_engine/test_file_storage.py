#!/usr/bin/python3
"""
Unit tests for the FileStorage class.

This module contains unit tests for the methods of the FileStorage class
from the models.engine.file_storage module.
"""

import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Set up the test case environment"""
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = "test_file.json"
        self.storage._FileStorage__objects = {}
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def tearDown(self):
        """Tear down the test case environment"""
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_all_method(self):
        """Test the all method of FileStorage"""
        self.assertEqual(self.storage.all(), {})

    def test_new_method(self):
        """Test the new method of FileStorage"""
        my_model = BaseModel()
        self.storage.new(my_model)
        key = f"{my_model.__class__.__name__}.{my_model.id}"
        self.assertIn(key, self.storage.all())

    def test_save_method(self):
        """Test the save method of FileStorage"""
        my_model = BaseModel()
        self.storage.new(my_model)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, "r") as f:
            content = json.load(f)
        key = f"{my_model.__class__.__name__}.{my_model.id}"
        self.assertIn(key, content)

    def test_reload_method(self):
        """Test the reload method of FileStorage"""
        my_model = BaseModel()
        self.storage.new(my_model)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        key = f"{my_model.__class__.__name__}.{my_model.id}"
        self.assertIn(key, self.storage.all())
        self.assertIsInstance(self.storage.all()[key], BaseModel)


if __name__ == '__main__':
    unittest.main()
