#!/ussr/bin/python3
"""
This module define the Satate class
"""
from models import base_model


class State(base_model.BaseModel):
    """
    State class represents a geographical state.
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
        Init the parent BaseModel
        """
        super().__init__(*args, **kwargs)
