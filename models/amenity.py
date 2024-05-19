#!/usr/bin/python3
"""
This module defines the Amenity class, which inherits from BaseModel.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class: inherits from BaseModel.
    Public class attributes:
        name (str): Amenity name.
    """
    name = ""
