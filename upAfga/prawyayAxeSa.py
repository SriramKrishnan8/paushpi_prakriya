#!/usr/bin/env python3

import os
import sys

import re

from sanXi.sanXi import terminal_sandhi
from saFjFA.saFjFA import ti
from saFjFA.prawyAhAra_saFjFA import get_letters
from util import axanwa_gaNa, xviwva_gaNa


def is_aByaswa(XAwu, gaNa):
    """ """ 

    # Paushpi Prakriya does not give the sUwra information regarding 
    # when a dviwwva occurs (i.e., with juhowyAxi gaNa (Slu) results 
    # in xviwwva)
    aByaswa = False
    if gaNa == "juhowyAxi":
        # SlO (6.1.90)
        aByaswa = True
    elif XAwu in ["jakR", "jAgq", "xarixrA", "cakAs", "SAs", "xIXI", "vevI"]:
        # jakRiwyAxayaH Rat (6.1.6)
        aByaswa = True
    else:
        aByaswa = False
    
    return aByaswa


def axaByaswAw(prawyaya):
    """ """ 

    # axaByaswAw (7.1.4)
    prawyaya = prawyaya.replace("J", "aw")
    
    return prawyaya


def AwmanepaxeRvanawaH(prawyaya):
    """ """ 

    # AwmanepaxeRvanawaH (7.1.5)
    prawyaya = prawyaya.replace("J", "aw")

    return prawyaya


def JoZnwaH(prawyaya):
    """ """ 

    # JoZnwaH (7.1.3)
    prawyaya = prawyaya.replace("J", "anw")

    return prawyaya


def replace_J(XAwu, prawyaya, gaNa, paxa):
    """ """ 

    if is_aByaswa(XAwu, gaNa):
        prawyaya = axaByaswAw(prawyaya)
    elif paxa == "Awmanepaxa" and not gaNa in axanwa_gaNa:
        prawyaya = AwmanepaxeRvanawaH(prawyaya)
    else:
        prawyaya = JoZnwaH(prawyaya)

    return prawyaya


def tiwa_AwmanepaxAnAM_tere(prawyaya, paxa, lakAra):
    """ """ 

    # tiwa AwmanepaxAnAM tere (3.4.79)
    if not (paxa == "parasmEpaxa") \
        and lakAra in [ "lat", "lot", "lit", "let", "lut", "lqt" ]:
        ti_term, ti_index = ti(prawyaya)
        prawyaya = prawyaya[:ti_index] + "e"
    
    return prawyaya


def Awo_fiwaH(prawyaya, gaNa):
    """ """ 

    # Awo fiwaH (7.2.81)
    # I have a doubt here
    if gaNa in axanwa_gaNa:
        prawyaya = prawyaya.replace("A", "iy", 1)
    
    return prawyaya


def lopo_vyorvali(prawyaya):
    """ """ 

    val = get_letters("val")[0]

    for x in val:
        prawyaya = prawyaya.replace("y" + x, x)
        prawyaya = prawyaya.replace("v" + x, x)
    
    return prawyaya


def WAsaH_se(prawyaya):
    """ """ 

    # WAsaH se (3.4.80)
    if prawyaya == "WAs":
        prawyaya = "se"
    
    return prawyaya


def lat(XAwu, prawyaya, paxa, lakAra, gaNa):
    """ """ 

    prawyaya = WAsaH_se(prawyaya)

    prawyaya = terminal_sandhi(prawyaya)

    prawyaya = replace_J(XAwu, prawyaya, gaNa, paxa)

    prawyaya = Awo_fiwaH(prawyaya, gaNa)

    prawyaya = lopo_vyorvali(prawyaya)

    prawyaya = tiwa_AwmanepaxAnAM_tere(prawyaya, paxa, lakAra)

    # Add conditions for aByaswa rule

    return prawyaya


def laf(prawyaya, paxa, lakAra, gaNa):
    """ """ 

    # Add laf conditions
    
    return prawyaya


def lot(prawyaya, paxa, lakAra, gaNa):
    """ """ 

    # Add lot conditions

    # Add conditions for aByaswa rule

    return prawyaya


def viXilif(prawyaya, paxa, lakAra, gaNa):
    """ """ 

    # Add viXilif conditions

    # Add conditions for aByaswa rule

    return prawyaya


def prawyaya_Axesa(XAwu, prawyaya, paxa, lakAra, gaNa):
    """ """ 

    if lakAra == "lat":
        prawyaya = lat(XAwu, prawyaya, paxa, lakAra, gaNa)
    elif lakAra == "lot":
        prawyaya = lot(prawyaya, paxa, lakAra, gaNa)
    elif lakAra == "laf":
        prawyaya = laf(prawyaya, paxa, lakAra, gaNa)
    elif lakAra == "viXilif":
        prawyaya = viXilif(prawyaya, paxa, lakAra, gaNa)
    else:
        pass

    return prawyaya

