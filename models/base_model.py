#!/usr/bin/python3
import uuid
import datetime
"""Base Model"""

class BaseModel:
    """Base Class"""

    def __init__(self):
        """Constructor"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """String representation"""
        return (f"{[self.__class__.__name__]} {(self.id)} {self.__dict__}")

    def save(self):
        """Update with current time"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Return dict representation"""
        dict = self.__dict__.copy()
        dict['__class__'] = self.__class__.__name__
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        return dict
