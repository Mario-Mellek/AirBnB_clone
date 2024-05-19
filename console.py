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

    def do_show(self, arg):
        """
            Prints the string representation of an instance
	    according to class name and id.
	"""
        args = shlex.split(arg)
        if self.validate_args(args, 2):
            key = f"{args[0]}.{args[1]}"
            instance = storage.all().get(key)
            if instance:
                print(instance)
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = shlex.split(arg)
        if self.validate_args(args, 2):
            key = f"{args[0]}.{args[1]}"
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def validate_args(self, args, expected_len):
        """Validates the arguments for the commands"""
        if not args:
            print("** class name missing **")
            return False
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return False
        if len(args) < expected_len:
            print("** instance id missing **")
            return False
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
