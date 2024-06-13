#!/usr/bin/env python3

import os
import sys

import re

from saFjFA.iw_saFjFA import handle_iw
from preprocess.changes import XAwu_changes
from util import anuxAwwa_iw_XAwus, svariwa_iw_XAwus, sArvaXAwuka_prawyayas


def XAwu_operations(XAwu):
    """ """ 
    
    # handle_iw
    xqSyarUpam, iw_types = handle_iw(XAwu)
    print(XAwu + " -> " + xqSyarUpam + " (" + ",".join(iw_types) + ")")
    
    # transformations to XAwus
    res, raw_XAwu = XAwu_changes(xqSyarUpam, iw_types)
    
    for new_XAwu, act in res:
        print(xqSyarUpam + " -> " + new_XAwu + " (" + act + ")")
    
    return raw_XAwu
    
    
def anuxAwwafiwa_Awmanepaxam(XAwu):
    """ """ 
    
    is_Awmanepaxa = False
    xqSyarUpam, iw_types = handle_iw(XAwu)
    
    if "fiw" in iw_types or XAwu in anuxAwwa_iw_XAwus:
        is_Awmanepaxa = True
    
    return is_Awmanepaxa
    

def svariwaFiwaH_karwraBiprAye_kriyAPale(XAwu):
    """ """ 
    
    is_uBayapaxa = False
    xqSyarUpam, iw_types = handle_iw(XAwu)
    
    if "Fiw" in iw_types or XAwu in svariwa_iw_XAwus:
        is_uBayapaxa = True
    
    return is_uBayapaxa
    

def paxanirNaya_viXi(XAwu):
    """ """ 
    
    paxa = "parasmEpaxa"
    if anuxAwwafiwa_Awmanepaxam(XAwu):
        paxa = "Awmanepaxa"
    elif svariwaFiwaH_karwraBiprAye_kriyAPale(XAwu):
        paxa = "uBayapaxa"
    else:
        paxa = "parasmEpaxa"
    
    return paxa


def get_prawyaya_type(lakAra):
    """ """ 

    prawyaya_type = "ArXaXAwuka"
    if lakAra in sArvaXAwuka_prawyayas: # Add let with sip condition
        prawyaya_type = "sArvaXAwuka"
    
    return prawyaya_type

