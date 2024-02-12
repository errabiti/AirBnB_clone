#!/usr/bin/python3
"""
The file_storage module contains the FileStorage class,
which serves as a mechanism for storing data in a JSON file (file.json)
"""

import json
from importlib import import_module


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the class attribute __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Add a new object to the objects class attribute.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Save the objects inside the objects class attr into a
        json file.
        """
        obj_dicts = {key: obj.to_dict()
                     for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dicts, f)

    def reload(self):
        """
        Retrive the objects from the json file
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                file_items = json.load(f)
                for obj_id, obj_dict in file_items.items():
                    class_name = obj_dict['__class__']
                    instance = getattr(import_module("models.base_model"),
                                       class_name)
                    FileStorage.__objects[obj_id] = instance(**obj_dict)
        except FileNotFoundError:
            pass
