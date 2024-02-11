import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    def setUp(self):
        """
        Set up test environment.
        """
        self.storage = FileStorage()

    def tearDown(self):
        """
        Clean up after the test.
        """
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all_empty(self):
        """
        Test the all method with an empty storage.
        """
        all_objects = self.storage.all()
        self.assertEqual(all_objects, {})

    def test_new_and_save(self):
        """
        Test creating a new object, adding it to storage, and saving it.
        """
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        file_path = FileStorage._FileStorage__file_path
        self.assertTrue(os.path.exists(file_path))

        with open(file_path, 'r') as file:
            data = json.load(file)
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.assertIn(key, data)

    def test_reload(self):
        """
        Test reloading objects from the file.
        """
        obj = BaseModel()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.storage.new(obj)
        self.storage.save()

        # Clear the current storage instance
        self.storage._FileStorage__objects = {}

        self.storage.reload()
        all_objects = self.storage.all()

        self.assertIn(key, all_objects)
        self.assertIsInstance(all_objects[key], BaseModel)
        self.assertEqual(all_objects[key].id, obj.id)

    def test_reload_nonexistent_file(self):
        """
        Test reloading when the file doesn't exist.
        Should not raise an error.
        """
        self.storage.reload()

    def test_reload_empty_file(self):
        """
        Test reloading when the file is empty.
        Should not raise an error.
        """
        # Create an empty file and reload, should not raise an error
        with open(FileStorage._FileStorage__file_path, 'w') as file:
            file.write('')
        self.storage.reload()


if __name__ == '__main__':
    unittest.main()

