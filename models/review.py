#!/usr/bin/python3

"""This module defines a class that inherits from BaseModel"""

from models.base_model import BaseModel

class Review(BaseModel):
    """A Review class
    Attributes:
        place_id (str): empty string, it will be the Place.id
        user_id (str): empty string, it will be the User.id
        text (str): empty string
    """

    place_id = ""
    user_id = ""
    text = ""
