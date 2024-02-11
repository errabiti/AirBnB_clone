# models/engine/file_storage.py

import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        obj_dicts = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dicts, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                file_items = json.load(f)
                for obj_id, obj_dict in file_items.items():
                    class_name = obj_dict['__class__']
                    instance = BaseModel(**obj_dict)
                    FileStorage.__objects[obj_id] = instance
        except FileNotFoundError:
            pass
