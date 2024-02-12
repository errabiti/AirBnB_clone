#!/usr/bin/puthon3
"""
This module has the TestUser class.
"""


import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    Test cases for the User class.
    """

    def test_user_creation(self):
        """
        Test case to verify the creation of a User instance.
        """

        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_attributes(self):
        """
        Test case to verify setting and getting of attributes.
        """

        user = User()
        user.email = "badr@example.com"
        user.password = "password123"
        user.first_name = "ayoub"
        user.last_name = "alx"

        self.assertEqual(user.email, "badr@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "ayoub")
        self.assertEqual(user.last_name, "alx")

    def test_user_to_dict(self):
        """
        Test case to verify conversion of User instance to dictionary.
        """

        user = User()
        user.email = "badr@example.com"
        user.password = "password123"
        user.first_name = "ayoub"
        user.last_name = "alx"

        user_dict = user.to_dict()

        expected_dict = {
            'id': user.id,
            'created_at': user.created_at.isoformat(),
            'updated_at': user.updated_at.isoformat(),
            'email': 'badr@example.com',
            'password': 'password123',
            'first_name': 'ayoub',
            'last_name': 'alx',
            '__class__': 'User'
        }

        self.assertEqual(user_dict, expected_dict)

    def test_user_str_representation(self):
        """
        Test case to verify string representation of User instance.
        """

        user = User()
        user.email = "badr@example.com"
        user.password = "password123"
        user.first_name = "ayoub"
        user.last_name = "alx"

        str_repr = str(user)

        expected_repr = "[User] ({}) {}".format(user.id, user.__dict__)

        self.assertEqual(str_repr, expected_repr)


if __name__ == '__main__':
    unittest.main()
