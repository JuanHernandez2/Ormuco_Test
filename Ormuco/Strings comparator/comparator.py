import os
import sys


class String_comparator:
    """
        Class String comparator to compare two strings and 
        return which is greater, less or equal than the other one.
    Attributes:
    string_1: String 1
    string_2: String 2
    """


    def __init__(self, s1, s2):
        """
         Class constructor
         Params:
         s1: string 1
         s2: string 2
        """
        self.string_1 = s1
        self.string_2 = s2


    def compare(self):
        """
        This function compares if both strings are greater, less or equal to the other one
        """
        if str(self.string_1) > str(self.string_2):
            return "{} is greater than {}".format(self.string_1, self.string_2)
        elif str(self.string_1) < str(self.string_2):
            return "{} is less than {}".format(self.string_1, self.string_2)
        else:
            return "{} is equal to {}".format(self.string_1, self.string_2)

    
    def check_strings(self):
        """ 
         Checks if the two strings are valid 
        """
        if self.string_1 is None or self.string_2 is None:
            raise ValueError("One of the arguments is missing or NoneType")

