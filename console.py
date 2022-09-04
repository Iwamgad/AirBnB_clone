#!/usr/bin/python3

"""This module defines a HBNB console class"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex
from models.user import User

class HBNBCommand(cmd.Cmd):
    """An HBNBCommand class
    Attributes:
        prompt (str): the command prompt.
    """
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def _quit(self, arg):
        """Exits the program"""
        return True

    def _EOF(self, arg):
        """Signals EOF to exit the program"""
        print("")
        return True

    def emptyLine(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass

    def _create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) 
        and prints the id
        Usage: create <class>
        """

        _arg = shlex.split(arg)
        if len(_arg) == 0:
            print("** class name missing **")
        elif _arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(_arg[0])().id)
            storage.save()

    def _show(self, arg):
        """Prints the string representation of an instance based on 
        the class name and id
        Usage: show <class> <id>
        """

        _arg = shlex.split(arg)
        dictObj = storage.all()
        if len(_arg) == 0:
            print("** class name missing **")
        elif _arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(_arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(_arg[0], _arg[1]) not in dictObj:
            print("** no instance found **")
        else:
            print(dictObj["{}.{}".format(_arg[0], _arg[1])])

    def _destroy(self, arg):
        """ Deletes an instance based on the class name and id
        Usage: destroy <class> <id>
        """

        _arg = shlex.split(arg)
        dictObj = storage.all()
        if len(_arg) == 0:
            print("** class name missing **")
        elif _arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(_arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(_arg[0], _arg[1]) not in dictObj.keys():
            print("** no instance found **")
        else:
            del dictObj["{}.{}".format(_arg[0], _arg[1])]
            storage.save()

    def _all(self, arg):
        """Prints all string representation of all instances 
        based or not on the class name
        Usage: all or all <class>
        """

        _arg = shlex.split(arg)
        if len(_arg) > 0 and _arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(_arg) > 0 and _arg[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(_arg) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def _update(self, arg):
        """Updates an instance based on the class name and id by 
        adding or updating attribute
        Usage: update <class> <id> <attribute_name> <attribute_value>
        """

        _arg = shlex.split(arg)
        dictObj = storage.all()

        if len(_arg) == 0:
            print("** class name missing **")
            return False
        if _arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(_arg) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(_arg[0], _arg[1]) not in dictObj.keys():
            print("** instance id missing **")
            return False
        if len(_arg) == 2:
            print("** attribute name missing **")
            return False
        if len(_arg) == 3:
            try:
                type(eval(_arg[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(_arg) == 4:
            obj = dictObj["{}.{}".format(_arg[0], _arg[1])]
            if _arg[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[_arg[2]])
                obj.__dict__[_arg[2]] = valtype(_arg[3])
            else:
                obj.__dict__[_arg[2]] = _arg[3]
        elif type(eval(_arg[2])) == dict:
            obj = dictObj["{}.{}".format(_arg[0], _arg[1])]
            for i, j in eval(_arg[2]).items():
                if (i in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[i]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[i])
                    obj.__dict__[i] = valtype(j)
                else:
                    obj.__dict__[i] = j
        storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
