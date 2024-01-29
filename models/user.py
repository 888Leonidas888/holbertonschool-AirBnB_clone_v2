#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    class User(BaseModel, Base):
        """This class defines a user by various attributes"""
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True, default="NULL")
        last_name = Column(String(128), nullable=True, default="NULL")
        places = relationship("Place", backref="user",
                              cascade="all, delete-orphan")
        reviews = relationship(
            'Review', cascade='all, delete-orphan', backref='user')
else:
    class User(BaseModel):
        """This class defines a user by various attributes"""
        email = ''
        password = ''
        first_name = ''
        last_name = ''
