import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

	def test_city_creation(self):
		city = City()
		self.assertIsInstance(city, City)
		self.assertIsInstance(city, BaseModel)
		self.assertTrue(hasattr(city, 'id'))
		self.assertTrue(hasattr(city, 'created_at'))
		self.assertTrue(hasattr(city, 'updated_at'))
		self.assertEqual(city.state_id, "")
		self.assertEqual(city.name, "")

	def test_city_attributes(self):
		city = City()
		city.state_id = "999"
		city.name = "tiznit"

		self.assertEqual(city.state_id, "999")
		self.assertEqual(city.name, "tiznit")

	def test_city_to_dict(self):
		city = City()
		city.state_id = "999"
		city.name = "tiznit"

		city_dict = city.to_dict()

		expected_dict = {
			'id': city.id,
			'created_at': city.created_at.isoformat(),
			'updated_at': city.updated_at.isoformat(),
			'state_id': '999',
			'name': 'tiznit',
			'__class__': 'City'
		}

		self.assertEqual(city_dict, expected_dict)

	def test_city_str_representation(self):
		city = City()
		city.name = "tiznit"

		str_repr = str(city)

		expected_repr = "[City] ({}) {}".format(city.id, city.__dict__)

		self.assertEqual(str_repr, expected_repr)


if __name__ == '__main__':
	unittest.main()

