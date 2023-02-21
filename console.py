#!/usr/bin/python3

import cmd
import re
import sys
from shlex import split

def parse(arg):
    curl_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBshell(cmd.Cmd):
    #"""Defines the holbertonbnd command interpreter"

    intro = "\nWelcome to holbertonbnb shell <input help for help or quit to exit>\n"
    prompt = "(hbnb)"

    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
            }

    def emptyline(self):
        """Do nothing with empty string"""
        pass

if __name__ == "__main__":
    HBNBshell().cmdloop()

