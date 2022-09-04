#!/usr/bin/python3

"""This module defines a class that inherits from BaseModel"""

from models.base_model import BaseModel

class User(BaseModel):
    """A User class
    Attributes:
        email(str) - empty string, the email of user
        password(str) - empty string, the password of a user
        first_name(str) - empty string, the first name of user
        last_name(str) - empty string, the last_name of User
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
