#!/usr/bin/python3
"""
This module defines the State class, which inherits from BaseModel.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    User class: inherits from BaseModel.
    Public class attributes:
        name (str): State name.
    """
    name = ""
