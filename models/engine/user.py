#!/usr/bin/python3
"""This module defines the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for managing user objects"""

    def __init__(self, *args, **kwargs):
        """Initialize User instance"""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

    def __str__(self):
        """Return the string representation of User"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        """Return a dictionary representation of User"""
        user_dict = super().to_dict()
        user_dict.update({
            "email": self.email,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name
        })
        return user_dict
