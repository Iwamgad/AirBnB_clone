#!/usr/bin/python3

"""This module defines a class that inherits from BaseModel"""

from models.base_model import BaseModel

class State(BaseModel):
    """A State class
    Attribute:
        name(str): empty string, the name of the state
    """

    name = ""
