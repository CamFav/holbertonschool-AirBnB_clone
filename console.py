import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program using Ctrl+D (EOF)"""
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
