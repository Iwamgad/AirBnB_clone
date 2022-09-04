#!/usr/bin/python3

"""This module defines a class that inherits from BaseModel"""

from models.base_model import BaseModel

class City(BaseModel):
    """A City class
    Attribute:
        state_id (str): empty string, it will be the state id.
        name (str): empty string, the name of the city.
    """

    state_id = ""
    name = ""
