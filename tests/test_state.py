import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):

	def test_state_creation(self):
		state = State()
		self.assertIsInstance(state, State)
		self.assertIsInstance(state, BaseModel)
		self.assertTrue(hasattr(state, 'id'))
		self.assertTrue(hasattr(state, 'created_at'))
		self.assertTrue(hasattr(state, 'updated_at'))
		self.assertEqual(state.name, "")

	def test_state_attributes(self):
		state = State()
		state.name = "Souss massaa"

		self.assertEqual(state.name, "Souss massaa")

	def test_state_to_dict(self):
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
		state = State()
		state.name = "Souss massaa"

		str_repr = str(state)

		expected_repr = "[State] ({}) {}".format(state.id, state.__dict__)

		self.assertEqual(str_repr, expected_repr)


if __name__ == '__main__':
	unittest.main()

