#!/usr/bin/env python3
"""modules for HBNBCommand"""
import cmd
import sys
from datetime import datetime
import json
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage as fs

"""HBNB Console"""


class HBNBCommand(cmd.Cmd):
    """Class to handle the custom project"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program using CTRL+D"""
        print()  # Print a newline before exiting
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
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
        args = line.split()

        if not line:
            print("** class name missing **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]

        try:
            # Show the string representation of an instance
            # based on class name and id
            cls = eval(class_name)
            instances = fs().all()
            key = "{}.{}".format(cls.__name__, instance_id)
            if key in instances:
                instance = instances[key]
                print(instance)
            else:
                print("** no instance found **")
                return

        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        if not line:
            print("** class name missing **")
            return

        args = line.split()

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]

        try:
            cls = eval(class_name)
            instances = fs().all()
            key = "{}.{}".format(cls.__name__, instance_id)

            if key in instances:
                instances.pop(key)
                fs().save()
            else:
                print("** no instance found **")

        except NameError:
            print("** class doesn't exist **")

    def do_all(self, line):
        # Print string representation of all instances
        # based on the class name, or all instances
        # Handle missing or non-existing class name
        try:
            args = line.split()
            if len(args) == 0:
                allItems = fs.all("")
            elif len(args) == 1:
                class_name = args[0]
                try:
                    class_obj = eval(class_name)
                    allItems = fs.all(class_name)
                except NameError:
                    print("** class doesn't exist **")
                    return
            else:
                print("** class doesn't exist **")
                return

            for key, value in allItems.items():
                print(value)

        except Exception as e:
            print(e)
            print("** class doesn't exist **")

    def do_update(self, line):
        args = line.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3]

        try:
            cls = eval(class_name)
            instances = fs().all()
            key = "{}.{}".format(cls.__name__, instance_id)

            if key in instances:
                instance = instances[key]

                
                setattr(instance, attribute_name, attribute_value)
                print(instance)
                instance.save()
            else:
                print("** no instance found **")

        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
