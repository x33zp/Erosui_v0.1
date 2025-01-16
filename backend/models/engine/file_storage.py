#!/usr/bin/python3
"""The manages serialization and deserialization
of instances to/from JSON file.
"""

import os
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Class that serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Get all instances stored in the file.
        """
        return FileStorage.__objects

    def new(self, obj):
        """Add a new instance to the storage.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves the serialized instances to the JSON file.
        """
        filename = FileStorage.__file_path
        json_data = {}

        for key, value in FileStorage.__objects.items():
            json_data[key] = value.to_dict()

        with open(filename, 'w') as jsonfile:
            json.dump(json_data, jsonfile)

    def reload(self):
        """Deserialize the JSON file and reload instances into memory.
        """
        filename = FileStorage.__file_path

        if not os.path.isfile(filename):
            return

        with open(filename, 'r') as jsonfile:
            obj_dict = json.load(jsonfile)
            for key, value in obj_dict.items():
                class_obj = eval(value["__class__"])(**value)
                FileStorage.__objects[key] = class_obj
