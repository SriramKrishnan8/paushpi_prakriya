#!/usr/bin/env python3

import os
import sys

import re

from saFjFA.iw_saFjFA import handle_iw
from preprocess.changes import XAwu_changes

def step_1(XAwu):
    """ """ 
    
    # handle_iw
    xqSyarUpam, iw_types = handle_iw(XAwu)
    print(XAwu + " -> " + xqSyarUpam + " (" + ",".join(iw_types) + ")")
    
    # transformations to XAwus
    res, raw_XAwu = XAwu_changes(xqSyarUpam, iw_types)
    
    for new_XAwu, act in res:
        print(xqSyarUpam + " -> " + new_XAwu + " (" + act + ")")
    
    return raw_XAwu
    
