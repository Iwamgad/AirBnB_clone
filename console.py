#!/usr/bin/python3
"""This module defines a HBNB console class"""

import cmd
from models import storage

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

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id
        Usage: create <class>
        """
        if len(args) == 0:
            print("** class name missing **")
        elif args != "BaseModel" :
            print("** class doesn't exist **")
        else:
            from models.base_model import BaseModel
            object = BaseModel()
            object.save()
            print(object.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on
        the class name and id
        Usage: show <class> <id>
        """
        argList = args.split()
       
        if len(argList) == 0:
            print("** class name missing **")
        elif argList[0] != "BaseModel" :
            print("** class doesn't exist **")
        elif len(argList) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(argList[0], argList[1]) not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()["{}.{}".format(argList[0], argList[1])])

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id
        Usage: destroy <class> <id>
        """
        argList = args.split()
       
        if len(argList) == 0:
            print("** class name missing **")
        elif argList[0] != "BaseModel" :
            print("** class doesn't exist **")
        elif len(argList) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(argList[0], argList[1]) not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()["{}.{}".format(argList[0], argList[1])]
            storage.save()
    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name
        Usage: all or all <class>
        """
        objList = []
        if len(args) == 0:
            for obj in storage.all().values():
                objList.append(str(obj))
        else:
            if args != "BaseModel":
                print("** class doesn't exist **")
                return
            for k, v in storage.all().items():
                className = k.split('.')[0]
                if className == args:
                    objList.append(str(v))
        print(objList)

    def do_update(self, args):
        """Updates an instance based on the class name and id by
        adding or updating attribute
        Usage: update <class> <id> <attribute_name> <attribute_value>
        """
        argList = args.split()

        if len(argList) == 0:
            print("** class name missing **")
        elif argList[0] != "BaseModel" :
            print("** class doesn't exist **")
        elif len(argList) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(argList[0], argList[1]) not in storage.all():
            print("** no instance found **")
        elif len(argList) < 3:
            print("** attribute name missing **")
        elif len(argList) < 4:
            print("** value missing **")
        else:
            className = argList[0]
            id = argList[1]
            key = argList[2]
            value = argList[3]

            objectKey = className + "." + id
            object = storage.all()[objectKey]
            object.__dict__[key] = eval(value)
            storage.save()   
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
