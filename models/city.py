#!/usr/bin/python3
"""
This module define the City class
"""

from models import base_model


class City(base_model.BaseModel):
    """
    This class represents a city.
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Init the parent BaseModel
        """
        super().__init__(*args, **kwargs)
