#!/usr/bin/env python3
import cmd
import sys
from datetime import datetime
import json
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage as fs
"""Modules for HBNBCommand"""


class HBNBCommand(cmd.Cmd):
    """Console"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program using CTRL+D"""
        print()  # Print a newline before exiting
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        if not line:
            print("** class name missing **")
            return

        try:
            myClass = "{}()".format(line.split(" ")[0])

            model = eval(myClass)
            model.save()
            print(model.id)

        except Exception as e:
            print("** class doesn't exist **")

    def do_show(self, line):
        # Handle missing or non-existing class name, id, or instance
        if not line:
            print("** class name missing **")
            return

        args = line.spit()

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]

        try:
            # Show the string representation of an instance
            # based on class name and id
            cls = eval(class_name)
            instance = fs.get(cls, instance_id)

            if instance is None:
                print("** no instance found **")
                return

            print(instance)
        except NameError:
            print("** class doesn't exist **")
        except Exception as e:
            print("** " + str(e))

    def do_destroy(self, line):
        if not line:
            print("** class name missing **")
            return

        try:
            print("Yo")
            # Destroy an instance based on class name and id
            # Save the change into the JSON file
            # Handle missing or non-existing class name, id, or instance
        except Exception as e:
            print("** " + str(e))

    def do_all(self, line):
        # Print string representation of all instances
        # based on the class name, or all instances
        # Handle missing or non-existing class name
        try:
            myClass = line.split(" ")[0]
            allItems = fs.all(myClass)
            
            for key, value in allItems.items():
                print(value)

        except Exception as e:
            print(e)
            print("** class doesn't exist **")

    def do_update(self, line):
        if not line:
            print("** class name missing **")
            return

        try:
            # Update an instance based on class name and id
            # by adding or updating an attribute
            # Save the change into the JSON file
            # Handle missing or non-existing class name, id, attribute name, or instance
            pass
        except Exception as e:
            print("** " + str(e))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
