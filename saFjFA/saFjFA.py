#!/usr/bin/env python3

import os
import sys

import re

from saFjFA.prawyAhAra_saFjFA import get_letters
from util import asawwva_cAxi, asawwva_prAxi, UryAxi_gaNa, ac, hal


def ti(term):
    """ Returns the ti of the given term along with the index
    """ 
    
    ac = get_letters("ac")[0]
    
    ti_term = []
    i = 0
    for char in list(reversed(term)):
        ti_term.append(char)
        i += 1
        if char in ac:
            break
        
    return "".join(list(reversed(ti_term))), len(term) - i
    

def upaXA(term):
    """ Returns the upaXA of the given term
    """
    
    if term[-1] == "z":
        upaXA_str = term[-3]
        upaXA_ind = len(term) - 1 - 2
    elif term[-2] == "z":
        upaXA_str = term[-3:-1]
        upaXA_ind = len(term) - 1 - 2
    else:
        upaXA_str = term[-2]
        upaXA_ind = len(term) - 1 - 1
    
    if term[upaXA_ind] in ac:
        upaXA_type = term[upaXA_ind] + "xupaXa"
    elif term[upaXA_ind] in hal:
        upaXA_type = term[upaXA_ind] + "upaXa"
    else:
        upaXA_type = "-"
    
    return upaXA_str, upaXA_ind, upaXA_type


def is_pluwa(term):
    """ Returns whether the given term is pluwa or not
    """ 
    
    pluwa = False
    if term.endswith("3") and term[-2] in get_letters("ac")[0]:
        pluwa = True
    
    return pluwa
    
    
def is_gawi(term):
    """ 
    """
    
    gawi = False
    
    # uryAxicvidAcaSca (1.4.61)
    if term in UryAxi_gaNa:
        gawi = True
    # Add cvi and dAc
    
    # anukaraNam cAniwiparam (1.4.62)
    
    # AxaranAxarayoH saxasaxI (1.4.63)
    if term.startswith("saw") or term.startswith("asaw"):
        gawi = True
    
    # BURaNeZlam (1.4.64)
    if term == "alam":
        gawi = True
    
    # anwaraparigrahe (1.4.65)
    if term == "anwar":
        gawi = True
    
    # kaNemanasI SraxXAprawIGawe (1.4.66)
    if term == "kaNe" or term == "manasI":
        gawi = True
    
    # purozvyayam (1.4.67)
    if term == "puras":
        gawi = True
    
    # aswaM ca (1.4.68)
    if term == "aswam":
        gawi = True
    
    # acCa gawyarWavaxeRu (1.4.69)
    
    # axoZnupaxeSe (1.4.70)
    if term == "axas":
        gawi = True
    
    # wiroZnwarXO (1.4.71)
    if term == "wiras":
        gawi = True
    
    # viBARA kqFi (1.4.72)
    
    # upAjeZnvAe (1.4.73)
    if term == "upAje" or term == "anvAje":
        gawi = True
    
    # sAkRAwpraBqwIni ca (1.4.74)
    # anawyAXAna urasimanasI (1.4.75)
    # maXye paxe nivacane ca (1.4.76)
    # niwyaM haswe pANAvupayamane (1.4.77)
    # prAXvam banXane (1.4.78)
    # jIvikopaniRaxAvpamye (1.4.79)
    
    return gawi


def is_nipAwa(term):
    """ Returns whether the given term is nipAwa or not
    """ 
    
    nipAwa = False
    
    if term in asawwva_cAxi:
        nipAwa = True
    
    if term in asawwva_prAxi:
        nipAwa = True
    
    if is_gawi(term):
        nipAwa = True
    
    return nipAwa


def is_ekAc(term):
    """ 
    """ 
    
    ac = get_letters("ac")[0]
    ac_count = 0
    for char in term:
        if char in ac:
            ac_count += 1
    
    return (ac_count == 1)
