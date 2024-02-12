#!/usr/bin/python3
"""
This module has the TestState class.
"""


import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    Test cases for the State class.
    """

    def test_state_creation(self):
        """
        Test case to verify the creation of a State instance.
        """

        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertEqual(state.name, "")

    def test_state_attributes(self):
        """
        Test case to verify setting and getting of attributes.
        """

        state = State()
        state.name = "Souss massaa"

        self.assertEqual(state.name, "Souss massaa")

    def test_state_to_dict(self):
        """
        Test case to verify conversion of State instance to dictionary.
        """

        state = State()
        state.name = "Souss massaa"

        state_dict = state.to_dict()

        expected_dict = {
                'id': state.id,
                'created_at': state.created_at.isoformat(),
                'updated_at': state.updated_at.isoformat(),
                'name': 'Souss massaa',
                '__class__': 'State'
        }

        self.assertEqual(state_dict, expected_dict)

    def test_state_str_representation(self):
        """
        Test case to verify string representation of State instance.
        """

        state = State()
        state.name = "Souss massaa"
        str_repr = str(state)
        expected_repr = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(str_repr, expected_repr)


if __name__ == '__main__':
    unittest.main()
