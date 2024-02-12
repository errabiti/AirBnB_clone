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

    def __init__(self, *args, **kwargs):
        """
        Init the parent BaseModel
        """
        super().__init__(*args, **kwargs)
