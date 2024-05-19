#!/usr/bin/python3
"""
This module defines the User class, which inherits from BaseModel.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class: inherits from BaseModel.
    Public class attributes:
        email (str): User email
        password (str): User password
        first_name (str): User first_name
        last_name (str): User last_name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
