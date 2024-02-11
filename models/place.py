#!/usr/bin/python3
"""
"""

from models import base_model

class Place(base_model.BaseModel):
    """
    Place class represents a location where guests can stay.
    """

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
