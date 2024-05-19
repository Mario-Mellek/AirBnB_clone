#!/usr/bin/python3
"""
    This module contains the entry point
    of the command interpreter.
"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter cmd class"""
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel}

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """Called when an empty line is entered."""
        pass

    def do_create(self, arg):
        """
            Creates a new instance of BaseModel,
            saves it and prints the id
        """
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return

        cls = self.classes[arg]
        cls_instance = cls()
        cls_instance.save()
        print(cls_instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
