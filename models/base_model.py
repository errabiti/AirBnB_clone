#!/usr/bin/python3
"""
This module contains the base model class
which will be inherited by the child classes.
"""


import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    This class is the base that all other models will extend
    """

    def __init__(self, *args, **kwargs):
        """
        Init the instance attribute
        """
        if kwargs:
            if kwargs['__class__']:
                del kwargs['__class__']
            self.set_args(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        save the ccurrent object in the dile.json
        """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def set_args(self, kwargs):
        """
        set the kwargs passed in the __init__ special method
        """
        self.id = str(kwargs['id'])
        self.created_at = datetime.fromisoformat(kwargs['created_at'])
        self.updated_at = datetime.fromisoformat(kwargs['updated_at'])

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
