#!/usr/bin/env python3

import os
import sys

import re

from saFjFA.iw_saFjFA import handle_iw
from preprocess.changes import XAwu_changes
from preprocess.preprocess import get_prawyaya_type
from util import wip_mas, wa_mahif
from upAfga.vikaraNa import get_vikaraNa
from upAfga.prawyayAxeSa import prawyaya_Axesa


def is_axanwa(XAwu):
    """ """ 

    return (XAwu[-1] == "a")


def assign_lakAra(lakAra):
    """ """ 

    sUwra = ""
    if lakAra == "lat":
        sUwra = "3.2.123" # varwamAne lat (3.2.123)
    elif lakAra == "laf":
        sUwra = "3.2.111" # varwamAne lat (3.2.111)
    # elif lakAra == "laf":
    #     sUwra = "3.2.123" # varwamAne lat (3.2.123)
    # elif lakAra == "lat":
    #     sUwra = "3.2.123" # varwamAne lat (3.2.123)
    # elif lakAra == "lat":
    #     sUwra = "3.2.123" # varwamAne lat (3.2.123)
    # elif lakAra == "lat":
    #     sUwra = "3.2.123" # varwamAne lat (3.2.123)
    # elif lakAra == "lat":
    #     sUwra = "3.2.123" # varwamAne lat (3.2.123)
    # elif lakAra == "lat":
    #     sUwra = "3.2.123" # varwamAne lat (3.2.123)
    # elif lakAra == "lat":
    #     sUwra = "3.2.123" # varwamAne lat (3.2.123)
    # elif lakAra == "lat":
    #     sUwra = "3.2.123" # varwamAne lat (3.2.123)
    else:
        pass

    return sUwra


def generate(upasarga, XAwu, gaNa, prayoga, lakAra, paxa):
    """ """ 

    prawyaya_type = get_prawyaya_type(lakAra)
    
    # get paxa information here. Temporarily receiving it from the user 
    wif_prawyayas = wip_mas if paxa == "parasmEpaxa" else wa_mahif
    
    res = []
    
    res.append((upasarga, XAwu, gaNa, "XAwu"))
    # iw 
    XAwu, XAwu_iw = handle_iw(XAwu)
    res.append((upasarga, XAwu, gaNa, "XAwu-iw"))
    # XAwu transformations 
    changes_res, XAwu = XAwu_changes(XAwu, XAwu_iw)
    res.append((upasarga, XAwu, gaNa, "XAwu-changes"))

    # lakAra assignment
    lakAra_sUwra = assign_lakAra(lakAra)
    res.append((upasarga, XAwu, gaNa, lakAra, lakAra_sUwra))
    
    # lasya (3.4.77)
    res.append((upasarga, XAwu, gaNa, lakAra, "lasya"))

    # iw 
    lakAra_iw, lakAra_iw_type = handle_iw(lakAra)
    res.append((upasarga, XAwu, gaNa, lakAra_iw, "lasya-iw"))
    
    # wipwasJi... (3.1.78)
    res.append((upasarga, XAwu, gaNa, wif_prawyayas, "wif"))

    # wifSiwsArvaXAwukam (3.4.113)
    res.append((upasarga, XAwu, gaNa, wif_prawyayas, prawyaya_type, "sArvaXAwuka"))

    # vikaraNa
    vikarana_res = get_vikaraNa(upasarga, XAwu, prawyaya_type, prayoga, gaNa)
    res.append((upasarga, XAwu, vikarana_res, wif_prawyayas, prawyaya_type, "vikaraNa"))

    # change ending s and r to H for the wif prawyayas
    wif_terminal_sandhi = [ prawyaya_Axesa(XAwu, wif, paxa, lakAra, gaNa, vikarana_res) for wif in wif_prawyayas ]
    res.append((upasarga, XAwu, vikarana_res, wif_terminal_sandhi, prawyaya_type, "wif-prawyayAxeSa"))

    # Next steps to be added...

    return res





