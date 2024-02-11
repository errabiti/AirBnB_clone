# models/base_model.py

from models import storage
import uuid
from datetime import datetime


class BaseModel:
    """
    This class is the base that all other models will extend
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the instance attributes
        """
        if kwargs:
            if '__class__' in kwargs:
                del kwargs['__class__']
            self.set_args(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Save the current object in the file.json
        """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def set_args(self, kwargs):
        """
        Set the kwargs passed in the __init__ special method
        """
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(kwargs.get('id', uuid.uuid4()))
        self.created_at = datetime.strptime(kwargs.get('created_at', datetime.now().strftime(date_format)), date_format)
        self.updated_at = datetime.strptime(kwargs.get('updated_at', datetime.now().strftime(date_format)), date_format)

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
