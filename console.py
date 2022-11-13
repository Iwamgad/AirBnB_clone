#!/usr/bin/python3
"""This module defines a HBNB console class"""

import cmd

class HBNBCommand(cmd.Cmd):
    """An HBNBCommand class
    Attributes:
        prompt (str): the command prompt.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exits the program"""
        return True

    def do_EOF(self, arg):
        """Exits the program with the command ctrl + D """
        print()
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
