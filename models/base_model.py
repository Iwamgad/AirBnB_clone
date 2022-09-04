#!/usr/bin/python3

"""This module defines all common attributes/methods for other classes"""

import models
from uuid import uuid4
from datetime import datetime

timeFormat = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """A BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel object
        Args:
            *arg (any): unused 
            **kwargs(dict): key/value pairs of attribute
        Raises:
            AttributeError: if attribute is null
        """

        if kwargs:
            for i, j in kwargs.items():
                if i != "__class__":
                    setattr(self, i, j)
            if hasattr(self, "created_at") and \
               type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs
                                                    ["created_at"], timeFormat)
            if hasattr(self, "updated_at") and \
               type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs
                                                    ["updated_at"], timeFormat)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """Returns the string representation of the BaseModel class"""
        clname = self.__class__.__name__
        return "[{}]({}) {}".format(clname, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        retDict = self.__dict__.copy()
        retDict["created_at"] = self.created_at.isoformat()
        retDict["updated_at"] = self.updated_at.isoformat()
        retDict["__class__"] = self.__class__.__name__
        return retDict
