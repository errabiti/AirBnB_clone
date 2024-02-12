#!usr/bin/python3
"""
This module define a User class.
"""


from models import base_model


class User(base_model.BaseModel):
    """
    User class
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Init the BaseModel args
        """
        super().__init__(*args, **kwargs)
