#!/usr/bin/python3

"""
A module containing the definition for the base class that defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """The base class that contains all common attributes/methods for other classes"""
    def __init__(self):
        """The initialization method for new instances"""
        self.id = str(uuid.uuid(4))
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """The custom __str__ called upon using the print() function"""
        return f"[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """The save function that saves to a file"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """A function that customizes the output of __dict__ attribute"""
        custom_dictionary = {}
        for key, value in elf.__dict__.items():
            if value is None:
                continue
            if key == "created_at" or key == "updated_at":
                value = value.isoformat()
            custom_dictionary[key] = value
        custom_dictionary["__class__"] = self.__class__.__name__
        return custom_dictionary
