#!/usr/bin/python3
"""The AirBnB clone"""
import sys
import datetime
import uuid
import models

class BaseModel:
    """The main class for all basic instructions"""
    def __init__(self, *args, **kwargs):
        """Initializes when an instance is created"""
        if kwargs:
            del kwargs['__class__']
            for key, value in kwargs.items():
                if isinstance(value, datetime.datetime):
                    dateobj = strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(val, key, dateobj)
        self.created_at = datetime.datetime.now()
        self.id = str(uuid.uuid4())
        self.updated_at = self.created_at
        models.storage.new(self)


    def __str__(self):
        """Returns a readable format of the instance created"""
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the time"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dicts representation of my instance attribute"""
        dict = {}
        dict['__class__'] = self.__class__.__name__
        for key, val in self.__dict__.items():
            if isinstance(val, datetime.datetime):
                dict[key] = val.isoformat()
            else:
                dict[key] = val
        return dict

if __name__ == '__main__':
    all_objs = storage.all()
    print("-- Reloaded objects --")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)

    print("-- Create a new object --")
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    my_model.save()
    print(my_model)