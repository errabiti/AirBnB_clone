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

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                # Check if the file is empty before attempting to load
                file_content = f.read()
                if file_content:
                    file_items = json.loads(file_content)
                    for obj_id, obj_dict in file_items.items():
                        class_name = obj_dict['__class__']
                        instance = getattr(importlib.import_module("models.base_model"), class_name)
                        self.__objects[obj_id] = instance(**obj_dict)
        except FileNotFoundError:
            pass  # Ignore if the file doesn't exist
        except json.decoder.JSONDecodeError:
            pass  # Ignore if the file is empty or not a valid JSON

    def test_reload_empty_file(self):
        """
        Test reloading when the file is empty.
        Should not raise an error.
        """
        # Check if the file exists and is not empty before reloading
        file_path = FileStorage._FileStorage__file_path
        if os.path.exists(file_path) and os.stat(file_path).st_size > 0:
            self.storage.reload()
        else:
            # File is empty or does not exist, no error should be raised
            self.storage.reload()

if __name__ == '__main__':
    unittest.main()

