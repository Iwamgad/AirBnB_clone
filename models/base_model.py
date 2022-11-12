#!/usr/bin/python3
"""This module defines all common attributes/methods for other classes"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel object
        Args:
            *arg (any): unused
            **kwargs(dict): key/value pairs of attribute
        Raises:
            AttributeError: if attribute is null
        """
        if kwargs:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                elif k == 'created_at' or k == 'updated_at':
                    self.__dict__[k] = datetime.strptime
                    (v, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[k] = v
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns the string representation of the BaseModel class"""
        className = self.__class__.__name__
        return f"[{className}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute updated_at with the
        current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        newDict = self.__dict__.copy()
        newDict["__class__"] = self.__class__.__name__
        newDict["created_at"] = self.created_at.isoformat()
        newDict["updated_at"] = self.updated_at.isoformat()
        return newDict
