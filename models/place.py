#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
from models.amenity import Amenity


if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity',
                          Base.metadata,
                          Column('place_id',
                                 String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id',
                                 String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True,
                                 nullable=False))

    class Place(BaseModel, Base):
        """ A place to stay """
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        reviews = relationship(
            'Review', cascade='all, delete-orphan', backref='place')
        amenities = relationship(
            'Amenity', secondary=place_amenity, viewonly=False)
else:
    class Place(BaseModel):
        """ A place to stay """
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """Return a list review obj"""
            from models import storage
            from models.review import Review

            list_review = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    list_review.append(review)

            return list_review

        @property
        def amenities(self):
            """Return a list of amenities obj"""
            from models import storage

            obj_amenities = []
            list_amenity = storage.all(Amenity).values()
            for amenity in list_amenity:
                if amenity.id in self.amenity_ids:
                    obj_amenities.append(amenity)

            return obj_amenities

        @amenities.setter
        def amenities(self, obj):
            """Add an new id to list"""
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
