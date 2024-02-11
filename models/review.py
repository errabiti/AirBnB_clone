#!/usr/bin/python3
"""
This modeule define  Review class
"""


from models import base_model

class Review(base_model.BaseModel):
    """
    Review class represents a feedback or review given to a place by a user.
    """

    place_id = ""
    user_id = ""
    text = ""
