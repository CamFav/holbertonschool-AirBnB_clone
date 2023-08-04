#!/usr/bin/python3
import uuid
from datetime import datetime
"""Base Model"""


class BaseModel:
    """Base Class"""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        from models.engine.file_storage import FileStorage
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            FileStorage().new(self)

    def __str__(self):
        """String representation"""
        myStr = "[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__)
        return myStr

    def save(self):
        """Update with current time"""
        import models
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return dict representation"""
        dict = self.__dict__.copy()
        dict['__class__'] = type(self).__name__
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        return dict
