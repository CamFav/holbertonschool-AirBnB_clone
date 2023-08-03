#!/usr/bin/env python3
import cmd
import sys
from datetime import datetime
import json


class HBNBCommand(cmd.Cmd):
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
            # Create an instance of the specified class
            # Save it to the JSON file
            # Print the instance id
            # Handle missing or non-existing class name
        except Exception as e:
            print("** " + str(e))

    def do_show(self, line):
        if not line:
            print("** class name missing **")
            return

        try:
            # Show the string representation of an instance
            # based on class name and id
            # Handle missing or non-existing class name, id, or instance
        except Exception as e:
            print("** " + str(e))

    def do_destroy(self, line):
        if not line:
            print("** class name missing **")
            return

        try:
            # Destroy an instance based on class name and id
            # Save the change into the JSON file
            # Handle missing or non-existing class name, id, or instance
        except Exception as e:
            print("** " + str(e))

    def do_all(self, line):
        # Print string representation of all instances
        # based on the class name, or all instances
        # Handle missing or non-existing class name
        pass

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
