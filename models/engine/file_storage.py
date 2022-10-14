#!/usr/bin/python3
""""""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classe = {'BaseModel': BaseModel}


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """method all of file storage"""
        return (self.__objects)

    def new(self, obj):
        """method new of file storage"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """method save of file storage"""
        dict = {}
        for key, value in self.__objects.items():
            dict[key] = value.to_dict()
        with open(self.__file_path, 'w', ) as file:
            json.dump(dict, file)
    
    def reload(self):
        """method reload of class reload"""
        dict = {'BaseModel':BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review}
        try: 
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                n_dict = json.loads(file.read())
                for key, value in n_dict.items():
                    self.new(dict[value['__class__']](**value))
        except IOError:
            pass
    