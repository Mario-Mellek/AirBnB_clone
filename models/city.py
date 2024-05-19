#!/usr/bin/python3
"""
This module defines the City class, which inherits from BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class: inherits from BaseModel.
    Public class attributes:
        state_id (str) State ID.
        name (str): City name.
    """
    state_id = ""
    name = ""
