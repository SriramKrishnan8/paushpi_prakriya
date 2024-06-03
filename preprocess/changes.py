#!/usr/bin/env python3

import os
import sys

import re

from saFjFA.iw_saFjFA import handle_iw
from saFjFA.saFjFA import upaXA
from util import ac, wa_varga, ta_varga


def XAwvAxeH_RaH_saH(term):
    """ sawva viXi """
    
    # XAwvAxeH RaH saH (6.1.164)
    ta_wa_map = {
        "t" : "w", "T" : "W", "d" : "x", "D" : "X", "N" : "n",
    }
    
    # subXAwuRTivuRvaRkAxInAM sawvaprawiReXo vakwavyaH (vArwika)
    exception_XAwus = [ "RvaRka", "RTivu" ]
    
    
    new_term = term[:]
    if term.startswith("R") and term not in exception_XAwus:
        if len(term) >= 2 and term[1] in ta_varga:
            new_term = "s" + ta_wa_map.get(term[1], term[1]) + term[2:]
        else:
            new_term = "s" + term[1:]
    
    return new_term


def RopaxeSa(term):
    """ for sawva viXi """
    
    new_term = XAwvAxeH_RaH_saH(term)
    is_RopaxeSa = False
    
    if new_term in [ "sekq", "sqp", "sq", "sqj", "swq", "swQ", "swyE" ]:
        new_term = term[:]
        is_RopaxeSa = False
    elif new_term in [ "RvaRka", "svix", "svax", "svaFj", "svap", "smif" ]:
        is_RopaxeSa = True
    else:
        if len(new_term) >= 2 and new_term[0] in [ "s", "R" ] and (new_term[1] in ac + wa_varga + [ "sa" ]):
            is_RopaxeSa = True
        else:
            new_term = term[:]
            is_RopaxeSa = False
    
    return is_RopaxeSa, new_term
    

def No_naH(term):
    """ """
    
    # No naH (6.1.65)
    
    new_term = term[:]
    
    if term[0] == "N":
        new_term = "n" + term[1:]
    
    return new_term
    

def Nopaxesa(term):
    """ """
    
    new_term = No_naH(term)
    is_NopaxeSa = False
    
    if new_term in [ "narx", "nAt", "nAW", "nAX", "nanx", "nakk", "nQ", "nqw" ]:
        is_NopaxeSa = False
    elif not new_term == term:
        is_NopaxeSa = True
    else:
        is_NopaxeSa = False
        
    return is_NopaxeSa, new_term
    

def numAgama(term, iw_types):
    """ """
    
    # ixiwo num XAwoH (7.1.58)
    # mixacoZnwyAwparaH (1.1.47)
    
    new_term = term[:]
    
    if "ixiw" in iw_types:
        tmp = ""
        for c in reversed(term):
            if c in ac:
                tmp += "n" + c
            else:
                tmp += c
        new_term = "".join(reversed(tmp))
    
    return new_term
    

def upaXAyAM_ca(term):
    """ """
    
    upaXA_str, upaXA_ind, upaXA_type = upaXA(term)
    
    i_u_map = { "i" : "I", "u" : "U" }
    
    new_term = term[:]
    
    if "r" in upaXA_str and upaXA_ind >= 1 and term[upaXA_ind - 1] in [ "i", "u" ]:
        new_term = term[:upaXA_ind - 1] + i_u_map.get(term[upaXA_ind - 1], term[upaXA_ind - 1]) + term[upaXA_ind:]
    
    return new_term
    

def XAwu_changes(XAwu, iw_types):
    """ 
    """ 
    
    res = []
    
    is_RopaxeSa, RopaxeSa_XAwu = RopaxeSa(XAwu)
    
    if is_RopaxeSa:
        res.append((RopaxeSa_XAwu, "RopaxeSa"))
    
    is_NopaxeSa, Nopaxesa_XAwu = Nopaxesa(RopaxeSa_XAwu)
    
    if is_NopaxeSa:
        res.append((Nopaxesa_XAwu, "Nopaxesa"))
    
    numAgama_XAwu = numAgama(Nopaxesa_XAwu, iw_types)
    
    if not numAgama_XAwu == Nopaxesa_XAwu:
        res.append((numAgama_XAwu, "numAgama"))
    
    new_XAwu = upaXAyAM_ca(numAgama_XAwu)
    
    if not new_XAwu == numAgama_XAwu:
        res.append((new_XAwu, "upaXA_xIrGa"))
    
    return res, new_XAwu
    


