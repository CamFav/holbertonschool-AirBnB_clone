#!/usr/bin/python3
import json
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
        obj_to_dict = FileStorage.__objects.copy()
        for key, value in obj_to_dict.items():
            obj_to_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_to_dict, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r", encoding='utf-8') as file:
                data = json.loads(file.read())
                for k in data.keys():
                    v = data[k]
                    FileStorage.__objects[k] = eval(v['__class__'])(**v)

                return FileStorage.__objects
        except:
            return {}
