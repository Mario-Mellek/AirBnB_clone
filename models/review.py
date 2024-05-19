#!/usr/bin/python3
"""
This module defines the Review class, which inherits from BaseModel.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class: inherits from BaseModel.
    Public class attributes:
        place_id (str): Place ID.
        user_id (str): User ID.
        text (str): Text.
    """
    place_id = ""
    user_id = ""
    text = ""
