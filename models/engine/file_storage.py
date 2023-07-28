#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
"""File Storage"""


class FileStorage:
    """File Storage Class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """All

        Returns:
            Dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """New

        Args:
            obj (key): id
        """
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        obj_to_dict = {}
        for key, value in obj_to_dict.items():
            obj_to_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_to_dict, file)

    def reload(self):
        classes = {
            'BaseModel': BaseModel
        }
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = value['__class__']
                    if class_name in classes:
                        cls = classes[class_name]
                        obj = cls(**value)
                        self.__objects[key] = obj
