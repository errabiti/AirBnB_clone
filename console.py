#!/usr/bin/python3
"""
The file_storage module contains the FileStorage class,
which serves as a mechanism for storing data in a JSON file (file.json)
"""


import json
import cmd
from models import storage
import models
import os
import importlib


class HBNBCommand(cmd.Cmd):
    """
    This class is the entry point
    """

    intro = ""
    prompt = "(hbnb) "
    class_names = ["User", "BaseModel",
                   "Place", "Review", "City", "Amenity", "State"]

    def do_create(self, model_name):
        """
        This method is  responsable of creating a new instance of
        the base model and save the object in a json file
        Usage <model_name>
        """
        if not model_name:
            print("** class name missing **")
            return
        path = os.getcwd() + "/models"
        for file_name in os.listdir(path):
            if not file_name.startswith("__"):
                if os.path.isfile(os.path.join(path, file_name)):
                    model_n = file_name[:-3]
                    try:
                        model = importlib.import_module(f"models.{model_n}")
                        if hasattr(model, model_name):
                            model = getattr(model, model_name)()
                            model.save()
                            print(model.id)
                    except ImportError:
                        print("** class doesn't exist **")

    def do_show(self, line):
        """
        Display a specifique object by its key
        Usage : show <model_name> <id>
        """
        args = line.split()
        if not args:
            print("** class name missing *")
        elif args[0] not in HBNBCommand.class_names:
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
        Destroy an object.
        """

        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_names:
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
        Display all objects.
        """

        args = line.split()
        if not args:
            for obj in storage.all().values():
                print(str(obj))
        elif args[0] not in HBNBCommand.class_names:
            print("** class doesn't exist **")
        else:
            for obj in storage.all().values():
                if args[0] in str(obj):
                    print(str(obj))

    def do_update(self, line):
        """
        update a specifique instance attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """

        args = line.split()
        if not args:
            print("** class name missing *")
        elif args[0] not in HBNBCommand.class_names:
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
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        exit the program
        """
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
