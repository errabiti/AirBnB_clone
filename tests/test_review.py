import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_review_creation(self):
        """Test creating a Review instance."""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_attributes(self):
        """Test setting and getting Review attributes."""
        review = Review()
        review.place_id = "123"
        review.user_id = "456"
        review.text = "Great experience"

        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "456")
        self.assertEqual(review.text, "Great experience")

    def test_review_to_dict(self):
        """Test converting Review instance to a dictionary."""
        review = Review()
        review.place_id = "123"
        review.user_id = "456"
        review.text = "Great experience"

        review_dict = review.to_dict()

        expected_dict = {
            'id': review.id,
            'created_at': review.created_at.isoformat(),
            'updated_at': review.updated_at.isoformat(),
            'place_id': '123',
            'user_id': '456',
            'text': 'Great experience',
            '__class__': 'Review'
        }

        self.assertEqual(review_dict, expected_dict)

    def test_review_str_representation(self):
        """Test the string representation of Review instance."""
        review = Review()
        review.text = "Great experience"

        str_repr = str(review)

        expected_repr = "[Review] ({}) {}".format(review.id, review.__dict__)

        self.assertEqual(str_repr, expected_repr)


if __name__ == '__main__':
    unittest.main()
