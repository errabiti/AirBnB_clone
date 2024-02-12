#!/usr/bin/python3
"""
This module has the TestPlace class.+
"""


import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """
    Test cases for the Place class.
    """

    def test_place_creation(self):
        """
        Test case to verify the creation of a Place instance.
        """

        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, 'id'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, 'updated_at'))
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place_attributes(self):
        """
        Test case to verify setting and getting of attributes.
        """

        place = Place()
        place.city_id = "123"
        place.user_id = "456"
        place.name = "Cozy Apart"
        place.description = "A comfortable place"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 40.7128
        place.longitude = -74.0060
        place.amenity_ids = ["wifi", "kitchen"]

        self.assertEqual(place.city_id, "123")
        self.assertEqual(place.user_id, "456")
        self.assertEqual(place.name, "Cozy Apart")
        self.assertEqual(place.description, "A comfortable place")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 40.7128)
        self.assertEqual(place.longitude, -74.0060)
        self.assertEqual(place.amenity_ids, ["wifi", "kitchen"])

    def test_place_to_dict(self):
        """
        Test case to verify conversion of Place instance to dictionary.
        """

        place = Place()
        place.city_id = "123"
        place.user_id = "456"
        place.name = "Cozy Apart"
        place.description = ''
        place.number_rooms = 0
        place.number_bathrooms = 0
        place.max_guest = 0
        place.price_by_night = 0
        place.latitude = 0.0
        place.longitude = 0.0
        place.amenity_ids = []

        place_dict = place.to_dict()

        expected_dict = {
            'id': place.id,
            'created_at': place.created_at.isoformat(),
            'updated_at': place.updated_at.isoformat(),
            'city_id': '123',
            'user_id': '456',
            'name': 'Cozy Apart',
            'description': '',
            'number_rooms': 0,
            'number_bathrooms': 0,
            'max_guest': 0,
            'price_by_night': 0,
            'latitude': 0.0,
            'longitude': 0.0,
            'amenity_ids': [],
            '__class__': 'Place'
        }
        self.assertEqual(place_dict, expected_dict)

    def test_place_str_representation(self):
        """
        Test case to verify string representation of Place instance.
        """

        place = Place()
        place.name = "Cozy Apart"
        str_repr = str(place)
        expected_repr = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(str_repr, expected_repr)


if __name__ == '__main__':
    unittest.main()
