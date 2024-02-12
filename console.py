#!/usr/bin/python3
"""
The file_storage module contains the FileStorage class,
which serves as a mechanism for storing data in a JSON file (file.json)
"""

import json
import importlib
import cmd
from models import base_model, storage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    This class is the entry point
    """

    intro = ""
    prompt = "(hbnb) "

    classes = ["BaseModel", "Place", "State", "City", "Amenity", "Review", "User"]  # Include User in the classes list

    def do_create(self, model_name):
        """
        Create a new instance of a base model and save it to a JSON file.
        Usage: create <model_name>
        """

        if not model_name:
            print("** class name missing **")
        elif model_name not in self.classes:
            print("** class doesn't exist **")
        else:
            my_model = getattr(importlib.import_module("models." + model_name.lower()), model_name)()
            my_model.save()
            print(my_model.id)

    def do_show(self, line):
        """
        Display a specific object by its key.
        Usage: show <model_name> <id>
        """

        args = line.split()
        if not args:
            print("** class name missing *")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_key = args[0] + "." + args[1]
            if obj_key in storage.all().keys():
                print(storage.all()[obj_key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Destroy an instance based on the class name and id.
        Usage: destroy <model_name> <id>
        """

        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            if obj_key in storage.all():
                del storage.all()[obj_key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Print all string representations of instances based on the class name.
        Usage: all <model_name>
        """

        args = line.split()
        if not args:
            for obj in storage.all().values():
                print(str(obj))
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            for obj in storage.all().values():
                if args[0] in str(obj):
                    print(str(obj))

    def do_update(self, line):
        """
        Update a specific instance attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """

        args = line.split()
        if not args:
            print("** class name missing *")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            if obj_key not in storage.all().keys():
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                obj = storage.all()[obj_key]
                if args[2] not in ["id", "created_at", "updated_at"]:
                    setattr(obj, args[2], args[3])
                    obj.save()

    def do_quit(self, line):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, line):
        """
        Exit the program.
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
