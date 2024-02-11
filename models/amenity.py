#!/usr/bin/python3
"""
This module define Amenity class .
"""

from models import base_model


class Amenity(base_model.BaseModel):
    """
    Amenity class represents an amenity that can be associated with a place.
    """
    name = ""
