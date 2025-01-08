#!/usr/bin/python3
"""The manages serialization and deserialization
of instances to/from JSON file.
"""

import os
import json
# from models.city import City
from models.user import User
# from models.place import Place
# from models.state import State
# from models.review import Review
# from models.amenity import Amenity
from models.base_model import BaseModel


class FileStorage:
    """Class that serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Get all instances stored in the file.
        """
        if cls is None:
            return FileStorage.__objects

        filtered_obj = {key: value for key, value in
                        FileStorage.__objects.items()
                        if isinstance(value, cls)}
        return filtered_obj

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

    def delete(self, obj=None):
        """_summary_

        Args:
            obj (_type_, optional): _description_. Defaults to None.
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del FileStorage.__objects[key]
        self.save()

    def close(self):
        """Calls the reload() method to deserialize JSON file to objects"""
        self.reload()
