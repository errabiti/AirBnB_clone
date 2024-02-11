import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_amenity_creation(self):
        """Test creating an Amenity instance."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertEqual(amenity.name, "")

    def test_amenity_attributes(self):
        """Test setting and getting Amenity attributes."""
        amenity = Amenity()
        amenity.name = "Pool"

        self.assertEqual(amenity.name, "Pool")

    def test_amenity_to_dict(self):
        """Test converting Amenity instance to a dictionary."""
        amenity = Amenity()
        amenity.name = "Gym"

        amenity_dict = amenity.to_dict()

        expected_dict = {
            'id': amenity.id,
            'created_at': amenity.created_at.isoformat(),
            'updated_at': amenity.updated_at.isoformat(),
            'name': 'Gym',
            '__class__': 'Amenity'
        }

        self.assertEqual(amenity_dict, expected_dict)

    def test_amenity_str_representation(self):
        """Test the string representation of Amenity instance."""
        amenity = Amenity()
        amenity.name = "Foot"

        str_repr = str(amenity)

        expected_repr = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)

        self.assertEqual(str_repr, expected_repr)


if __name__ == '__main__':
    unittest.main()
