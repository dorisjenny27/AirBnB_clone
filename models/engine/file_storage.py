#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    class_dict = {
        "BaseModel": BaseModel
    }

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj
    
    def save(self):
        with open(self.__file_path, "w") as f:
            json_dict = {k:v.to_dict() for k, v in self.__objects.items()}
            json.dump(json_dict, f)
    
    def reload(self):
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                json_dict = json.load(f)
            for k, v in json_dict.items():
                self.__objects[k] = self.class_dict[v['__class__']](**v)
        except:
            pass

