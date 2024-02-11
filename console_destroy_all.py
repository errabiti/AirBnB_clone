#!/usr/bin/python3
"""
The file_storage module contains the FileStorage class, which serves as a mechanism for storing data in a JSON file (file.json)
"""

import json
import importlib
import cmd
from models import base_model, storage


class HBNBCommand(cmd.Cmd):
	"""
	This class is the entry point
	"""

	intro = ""
	prompt = "(hbnb) "

	def do_create(self, model_name):
		if not model_name:
			print("** class name missing **")
		elif model_name not in dir(base_model):
			print("** class doesn't exist **")
		else:
			my_model = getattr(base_model, model_name)()
			my_model.save()
			print(my_model.id)

	def do_show(self, line):
		print(storage.all())

	def do_destroy(self, line):
		args = line.split()
		if not args:
			print("** class name missing **")
		elif args[0] not in dir(base_model):
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
		args = line.split()
		if not args:
			for obj in storage.all().values():
				print(str(obj))
		elif args[0] not in dir(base_model):
			print("** class doesn't exist **")
		else:
			for obj in storage.all().values():
				if args[0] in str(obj):
					print(str(obj))
					
	def do_quit(self, line):
		"""
		Quit command to exit the program
		"""
		return True

	def do_EOF(self, line):
		"""
		exit the program
		"""
		return True


if __name__ == '__main__':
	HBNBCommand().cmdloop()
