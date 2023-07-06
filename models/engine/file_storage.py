#!/usr/bin/python3
import json
"""File Storage"""


class FileStorage:
    """File Storage Class"""
    __file_path = "file.json"
    __objects = []

    def all(self):
        """All

        Returns:
            Dictionary __objects
        """
        return self.__objects.__dict__

    def new(self, obj):
        """New

        Args:
            obj (key): id
        """
        self.__objects = obj.__class__.__name__

    def save(self):
        serialiazed_data = json.dumps(self.__objects)

        with open(self.__file_path, 'w') as file:
            file.write(serialiazed_data)

    def reload(self):
        if self.__file_path:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
            return data
        else:
            return None
