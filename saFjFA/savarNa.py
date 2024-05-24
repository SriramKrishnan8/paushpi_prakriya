#!/usr/bin/env python3

import os
import sys

import re


def get_savarNa(character):
    """ Returns all the savarNas of the give character
    """ 
    
    savarNa_dict = {
        "a" : [ "a", "A" ],
        "A" : [ "a", "A" ],
        "i" : [ "i", "I" ],
        "I" : [ "i", "I" ],
        "u" : [ "u", "U" ],
        "U" : [ "u", "U" ],
        "q" : [ "q", "Q", "L" ],
        "Q" : [ "q", "Q", "L" ],
        "L" : [ "q", "Q", "L" ],
        "e" : [ "e", "o" ],
        "o" : [ "e", "o" ],
        "E" : [ "E", "O" ],
        "O" : [ "E", "O" ],
        
    }
    
    return savarNa_dict.get(character, "")
