#!/usr/bin/env python3

import os
import sys

import re

from util import ac, hal, anunAsika, wa_varga, XAwus_list, viBakwi_saFjFA, \
    R_prawyayas, all_prawyayas, ca_varga, ta_varga, ka_varga, waxXiwa_prawyayas


def is_upaxeSa(term):
    """ Checks if the given term is an upaxeSa or not
    """
    
    # check for the following
    # mAheSvara sUwra
    # all_prawyayas
    # all_AxeSas
    # all_Agamas
    # XAwus_list
    
    # Temporarily
    
    return True


def is_prawyaya(term):
    """ Checks if the given term is an upaxeSa or not
    """
    
    return term in all_prawyayas


def wasya_lopaH(term, indices):
    """ Deletes the characters in the indices specified
    """
    
    new_term = ""
    for i in range(len(term)):
        if not i in indices:
            new_term = new_term + term[i]
    
    return new_term


def anunAsika_ac(term):
    """ Mark the anunAsika_ac in the given term
        
        returns the corresponding indices
    """
    
    indices = []
    for vow in ac:
        iw_start_indices = [m.start() for m in re.finditer(vow + anunAsika, term)]
        
        if len(iw_start_indices) == 0:
            continue
            
        for ind in iw_start_indices:
            # This condition is proposed here to avoid marking of the indices
            # in cases where the term ends with a vowel followed by z followed
            # by r. This is captured in the next sUwra "halanwyam"
            if ind == len(term) - 3 and term.endswith("r"):
                pass
            else:
                indices += [ ind, ind + 1 ]
    
    iw_chars = [term[x] for x in indices[0::2]]
    iw_types = [x + "xiw" for x in iw_chars]
    
    return indices, iw_types
    

def na_viBakwO_wusmAH(term):
    """ Checks the corresponding sUwra and returns True or False
        accordingly. True indicates the iw can be obtained. False
        indicates not.
    """
    
    iw_obtained = True
    if term in viBakwi_saFjFA and (any([term.endswith(x) for x in (wa_varga + ["s", "m"])])):
        iw_obtained = False
    
    return iw_obtained


def halanwyam(term):
    """ Mark the hal at the end of the given term
    """
    
    indices = []
    iw_types = []
    length = len(term) - 1
    if term.endswith("ir") or term.endswith("izr"):
        # Technically we are checking the halanwya here, but for terms
        # like Ciwizr, the previous sUwra "upaxeSeZjanunAsika iw" marks
        # the indices of "iz", and the current sUwra marks the r
        indices = [ length - 1, length ]
        iw_types = [ "iriw" ]
    elif (term[-1] in hal) and na_viBakwO_wusmAH(term):
        indices = [ length ]
        iw_types = [ term[-1] + "iw" ]
    else:
        pass
        
    return indices, iw_types


def AxirFitudavaH(term):
    """ Mark initial index if it starts with "Fi", "tu", "du"
        (specifically for XAwus)
    """
    
    indices = []
    iw_types = []
    
    map_Fi_tu_du = {
        "Fi" : "FIw", "tu" : "tviw", "du" : "dviw"
    }
    
    if term in XAwus_list:
        if any([term.startswith(x) for x in ["Fi", "tu", "du"]]):
            indices = [ 0, 1 ]
            iw_types = [ map_Fi_tu_du[term[0:2]] ]
    
    return indices, iw_types


def RaH_prawyayasya(term):
    """ Mark the initial index if the term is a prawyaya
        and startswith R
    """
    
    indices = []
    iw_types = []
    if term in R_prawyayas or term.startswith("R"):
        indices = [ 0 ]
        iw_types = [ "Riw" ]
    
    return indices, iw_types


def cutU(term):
    """ Mark the initial index if the term starts with 
        ca-varga or ta-varga
    """
    
    indices = []
    iw_types = []
    if any([term.startswith(x) for x in (ca_varga + ta_varga)]):
        indices = [ 0 ]
        iw_types = [ term[0] + "iw" ]
    
    return indices, iw_types


def laSakvawaxXiwe(term):
    """ Mark the initial index if term is not a taddhita pratyaya
        and starts with l, S and one of ka-varga
    """
    
    indices = []
    iw_types = []
    if any([term.startswith(x) for x in (ka_varga + [ "l", "S" ])]) \
        and (term not in waxXiwa_prawyayas):
        indices = [ 0 ]
        iw_types = [ term[0] + "iw" ]
    
    return indices, iw_types


def get_iw(term):
    """ Sequence of methods to call for identifying iw substrings,
        removing them and generating the type of iw
    """
    
    indices = []
    iw_types = []
    
    if not is_upaxeSa:
        return indices, iw_types
    
    i_a, t_a = anunAsika_ac(term)
    i_h, t_h = halanwyam(term)
    i_A, t_A = AxirFitudavaH(term)
    
    if not term in all_prawyayas:
        indices = i_a + i_h + i_A
        iw_types = t_a + t_h + t_A
        
        return indices, iw_types
    
    i_R, t_R = RaH_prawyayasya(term)
    i_c, t_c = cutU(term)
    i_l, t_l = laSakvawaxXiwe(term)
    
    indices = i_a + i_h + i_A + i_R + i_c + i_l
    iw_types = t_a + t_h + t_A + t_R + t_c + t_l
    
    return indices, iw_types
    
    
def handle_iw(term):
    """ Sequence of methods to call for identifying iw substrings,
        removing them and generating the type of iw
    """
    
    indices, iw_types = get_iw(term)
    
    xqSyarUpam = wasya_lopaH(term, indices)
    
    return xqSyarUpam, iw_types
    

def print_iw(term):
    """ """
    
    xqSyarUpam, iw_types = handle_iw(term)
    print(term + " -> " + xqSyarUpam + " (" + ",".join(iw_types) + ")")
    

