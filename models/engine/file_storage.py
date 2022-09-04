#!/usr/bin/python3

"""This module defines the FileStorage class"""

import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.state import State


class FileStorage:
    """Represent an abstracted storage engine
    Attributes:
        __file_path (str): path to the JSON file 
        __objects (dict): empty but will store all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        cname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(cname, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        odict = FileStorage.__objects
        # changing the json input into a dict
        dictObj = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as j:
            json.dump(dictObj, j)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. 
        If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path) as f:
                dictObj = json.load(f)
                for obj in dictObj.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    # unpacking the dict(**)
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
