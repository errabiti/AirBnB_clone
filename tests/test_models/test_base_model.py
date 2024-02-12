#!/usr/bin/env python3
"""
This module has all the test cases for the base model
"""


from models import base_model
import time
import unittest


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def setUp(self):
        """
        Set up the test fixture.
        This method is called before each test function.
        """

        self.base_model = base_model.BaseModel()

    def test_save(self):
        """
        Test case to verify the save method updates the 'updated_at' attribute.
        """

        initial_updated_value = self.base_model.updated_at
        time.sleep(5)
        self.base_model.save()
        self.assertNotEqual(initial_updated_value, self.base_model.updated_at)

    def test_to_dict(self):
        """
        Test case to verify the to_dict method returns a dictionary.
        """

        self.assertTrue(isinstance(self.base_model.to_dict(), dict))

    def test_attr_type(self):
        """
        Test case to verify the data types of
        attributes in the dictionary returned by to_dict.
        """

        instance_attr = self.base_model.to_dict()
        for attr_key, attr_value in instance_attr.items():
            if attr_key in ["id", "created_at", "updated_at"]:
                self.assertTrue(isinstance(attr_value, str),
                                f"Attribute '{attr_key}' should be a string")


if __name__ == "__main__":
    unittest.main()
