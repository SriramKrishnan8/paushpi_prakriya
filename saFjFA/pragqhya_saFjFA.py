#!/usr/bin/env python3

import os
import sys

import re

from saFjFA.saFjFA import is_nipAwa
from saFjFA.prawyAhAra_saFjFA import get_letters


def is_pragqhya(term):
    """ Returns whether the given term is a pragqhya or not
    """ 
    
    pragqhya = False
    
    ac = get_letters("ac")[0]
    
    # ixUxvexvivacanam pragqhyam (1.1.11)
    if any([term.endswith(x) for x in [ "I", "U", "e" ]]):
        # Add condition for checking if these are xvivacana forms
        pragqhya = True
    
    # axaso mAw (1.1.12)
    lst = [ "amU", "amI" ]
    if term in lst:
        pragqhya = True
    
    # Se (1.1.13)
    if term == "Se":
        pragqhya = True
        
    # nipAwa ekAjanAf (1.1.14)
    if is_nipAwa(term) and term in ac and not term == "A":
        pragqhya = True
    
    # ow (1.1.15)
    if is_nipAwa(term) and term[-1] == "o":
        pragqhya = True
    
    # sambuxXO SAkalyasyewAvanArRe (1.1.16)
    # check for samboxana-ekavacana form (mostly ukArAnwa Sabxa)
    # hence requires morphological analyses
    # next term should be iwi
    # not in Vedic context
    if term[-1] == "o":
        pragqhya = True
    
    # uFaH (1.1.17)
    # Uz iwi (not in Vedic context )
    if term == "uF":
        pragqhya = True
    
    # Uz (1.1.18)
    # Uz iwi (not in Vedic context )
    if term == "uF":
        pragqhya = True
    
    # IxUwO ca sapwamyarWe (1.1.19)
    # stem(term) should end in I or U
    
    return pragqhya
