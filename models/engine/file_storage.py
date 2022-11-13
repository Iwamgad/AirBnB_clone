#!/usr/bin/python3
"""This module defines the FileStorage class"""
from json import dump, load
from os.path import exists


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
        key = type(obj).__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        from models.base_model import BaseModel
        fileName = FileStorage.__file_path
        objects = FileStorage.__objects
        objDict = {}

        for k, v in objects.items():
            objDict[k] = v.to_dict()
        with open(fileName, 'w', encoding='utf8') as file:
            dump(objDict, file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        from models.base_model import BaseModel
        fileName = FileStorage.__file_path
        if exists(fileName):
            with open(fileName) as file:
                objDict = load(file)

            for v in objDict.values():
                del v['__class__']
                obj = BaseModel(**v)
                self.new(obj)
        else:
            return
                
