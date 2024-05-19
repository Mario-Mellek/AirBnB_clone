#!/usr/bin/python3
"""This module sets up the storage engine for the application"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
