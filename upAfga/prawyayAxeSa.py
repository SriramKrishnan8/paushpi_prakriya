#!/usr/bin/env python3

import os
import sys

import re

from sanXi.sanXi import terminal_sandhi
from saFjFA.saFjFA import ti
from saFjFA.iw_saFjFA import handle_iw
from saFjFA.prawyAhAra_saFjFA import get_letters
from util import axanwa_gaNa, xviwva_gaNa, fiw_lakAra, hal


def is_aByaswa(XAwu, gaNa):
    """ """ 

    # Paushpi Prakriya does not give the sUwra information regarding 
    # when a dviwwva occurs (i.e., with juhowyAxi gaNa (Slu) results 
    # in xviwwva) - while mentioning about aByaswa in lat-prawyayAxeSa.
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


def replace_J_lat(XAwu, prawyaya, gaNa, paxa, lakAra, vikaraNa):
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


def lat(XAwu, prawyaya, paxa, lakAra, gaNa, vikaraNa):
    """ """ 

    prawyaya_orig = prawyaya
    
    prawyaya = handle_iw(prawyaya)[0]

    if prawyaya in [ "wi", "si", "mi"]:
        # do nothing
        pass
    
    if prawyaya in [ "was", "Was", "vas", "mas" ]:
        prawyaya = terminal_sandhi(prawyaya)
    
    if prawyaya == "Wa":
        # do nothing
        pass

    if prawyaya == "Ji":
        prawyaya = JoZnwaH(prawyaya)
    
    if prawyaya in [ "wa", "Xvam", "i", "vahi", "mahi" ]:
        prawyaya = tiwa_AwmanepaxAnAM_tere(prawyaya, paxa, lakAra)
    
    if prawyaya in [ "AwAm", "AWAm" ]:
        if gaNa in axanwa_gaNa:
            prawyaya = Awo_fiwaH(prawyaya, gaNa)
            prawyaya = lopo_vyorvali(prawyaya)
        else:
            pass
        prawyaya = tiwa_AwmanepaxAnAM_tere(prawyaya, paxa, lakAra)
    
    if prawyaya == "WAs":
        prawyaya = WAsaH_se(prawyaya)
    
    if prawyaya == "Ja":
        if gaNa in axanwa_gaNa:
            prawyaya = JoZnwaH(prawyaya)
        else:
            prawyaya = AwmanepaxeRvanawaH(prawyaya)
        prawyaya = tiwa_AwmanepaxAnAM_tere(prawyaya, paxa, lakAra)
    
    # The following can be clubbed with the previous case but the 
    # Paushpi Prakriya has provided it as a last condition. 
    # So we did not move it above. This prevents the entire structure
    # to be converted into an if-elif-else condition statements.  
    # Similar issue is there for other lakAras also.  
    if prawyaya_orig == "Ji":
        if is_aByaswa(XAwu, gaNa):
            prawyaya = axaByaswAw(prawyaya_orig)
    
    # The above is as prescribed in Paushpi Prakriya.
    # Alternate procedure is described below.
    # Both work the same. The difference lies in the abstraction
    # and sharing of code.  

    # prawyaya = WAsaH_se(prawyaya)

    # prawyaya = terminal_sandhi(prawyaya)

    # prawyaya = replace_J_lat(XAwu, prawyaya, gaNa, paxa, lakAra, vikaraNa)

    # prawyaya = Awo_fiwaH(prawyaya, gaNa)

    # prawyaya = lopo_vyorvali(prawyaya)

    # prawyaya = tiwa_AwmanepaxAnAM_tere(prawyaya, paxa, lakAra)

    return prawyaya


def iwaSca(paxa, prawyaya):
    """ """ 

    # iwaSca (3.4.100)
    if paxa == "parasmEpaxa" and prawyaya != "mip":
        k = prawyaya.rfind("i")
        if k != -1:
            prawyaya = prawyaya[:k] + prawyaya[k+1:]
    
    return prawyaya


def wasWasWamipAM_wAnwanwAmaH(paxa, prawyaya):
    """ """ 

    # wasWasWamipAM_wAnwanwAmaH (3.2.101)
    map_ = {
        "was" : "wAm",
        "Was" : "wam",
        "Wa" : "wa",
        "mip" : "am",
    }
    if paxa == "parasmEpaxa" and prawyaya in [ "was", "Was", "Wa", "mip" ]:
        prawyaya = map_.get(prawyaya, prawyaya)
    
    return prawyaya


def niwyaM_fiwaH(paxa, prawyaya):
    """ """ 

    # niwyam fiwaH (3.2.99)
    if paxa == "parasmEpaxa" and prawyaya in [ "vas", "mas" ]:
        prawyaya = prawyaya.replace("s", "")
    
    return prawyaya


def sijaByaswavixiByaSca(XAwu, prawyaya, vikaraNa, gaNa):
    """ """ 

    if "sic" in vikaraNa or XAwu == "vix" or is_aByaswa(XAwu, gaNa):
        new_prawyaya = "jus"
        new_prawyaya = handle_iw(new_prawyaya)[0]
        new_prawyaya = terminal_sandhi(new_prawyaya)
        # We could have directly assigned "uH" to prawyaya but we 
        # will not know that we got uH from "jus", which is also 
        # mentioned in Paushpi Prakriya.  
        # Temporarily assigned directly as there is some problem
        # in handling the iw
        # should jus be added into the list of vibhakti?
        new_prawyaya = "uH"
        prawyaya = new_prawyaya # "uH"


    return prawyaya


def saMyogAnwasya_lopaH(prawyaya):
    """ """ 

    if len(prawyaya) > 2 and prawyaya[-1] in hal and prawyaya[-2] in hal:
        prawyaya = prawyaya[:-1]
    
    return prawyaya


def replace_J_laf(XAwu, prawyaya, gaNa, paxa, vikaraNa):
    """ """ 

    if is_aByaswa(XAwu, gaNa):
        prawyaya = sijaByaswavixiByaSca(XAwu, prawyaya, vikaraNa, gaNa)
    elif paxa == "Awmanepaxa" and not gaNa in axanwa_gaNa:
        prawyaya = AwmanepaxeRvanawaH(prawyaya)
    else:
        prawyaya = JoZnwaH(prawyaya)
    
    return prawyaya


def laf(XAwu, prawyaya, paxa, lakAra, gaNa, vikaraNa):
    """ """ 

    # Add laf conditions
    prawyaya_orig = prawyaya

    # It is not mentioned in the Paushpi PrakriyA that we 
    # handle iw, but we are doing it as the next steps
    # involve both the original prawyayas and also the ones
    # after handling iw. 
    prawyaya = handle_iw(prawyaya)[0]

    # parasmEpaxa

    # Here, Paushpi PrakriyA mentions "wi" and "si" instead 
    # of "wip" and "sip"
    if prawyaya in [ "wi", "si" ]:
        prawyaya = iwaSca(paxa, prawyaya)
    
    if prawyaya == "Ji":
        prawyaya = JoZnwaH(prawyaya)
        prawyaya = iwaSca(paxa, prawyaya)
        prawyaya = saMyogAnwasya_lopaH(prawyaya)
    
    # Here the Paushpi prakriyA mentions the original forms 
    # of the prawyayas
    if prawyaya_orig in [ "was", "Was", "Wa", "mip" ]:
        prawyaya = wasWasWamipAM_wAnwanwAmaH(paxa, prawyaya_orig)
    
    if prawyaya in [ "vas", "mas" ]:
        prawyaya = niwyaM_fiwaH(paxa, prawyaya)
    
    # Awmanepaxa
    
    if prawyaya in [ "wa", "Xvam" ]:
        # do nothing
        pass
    
    if prawyaya in [ "AwAm", "AWAm" ]:
        if gaNa in axanwa_gaNa:
            prawyaya = Awo_fiwaH(prawyaya, gaNa)
            prawyaya = lopo_vyorvali(prawyaya)
        else:
            pass
    
    if prawyaya == "Ja":
        if gaNa in axanwa_gaNa:
            prawyaya = JoZnwaH(prawyaya)
        else:
            prawyaya = AwmanepaxeRvanawaH(prawyaya)
    
    if prawyaya_orig == "Ji":
        if is_aByaswa(XAwu, gaNa):
            prawyaya = sijaByaswavixiByaSca(XAwu, prawyaya_orig, vikaraNa, gaNa)
    
    # This is not mentioned in Paushpi PrakriyA explicitly. 
    # But the final form has handled the terminal Sandhi. 
    if prawyaya == "WAs":
        prawyaya = terminal_sandhi(prawyaya)
    
    # The above is as prescribed in Paushpi Prakriya.
    # Alternate procedure is described below.
    # Both work the same. The difference lies in the abstraction
    # and sharing of code.  
    
    # prawyaya = replace_J_laf(XAwu, prawyaya, gaNa, paxa, vikaraNa)
    
    # prawyaya = iwaSca(paxa, prawyaya)

    # if paxa == "parasmEpaxa":
    #     prawyaya = wasWasWamipAM_wAnwanwAmaH(paxa, prawyaya_orig)
    #     prawyaya = niwyaM_fiwaH(paxa, prawyaya)
    # elif paxa == "Awmanepaxa":
    #     prawyaya = Awo_fiwaH(prawyaya, gaNa)
    #     prawyaya = lopo_vyorvali(prawyaya)
    
    # prawyaya = saMyogAnwasya_lopaH(prawyaya)

    # prawyaya = terminal_sandhi(prawyaya)

    return prawyaya


def eruH(prawyaya):
    """ 3.4.86 """

    prawyaya = prawyaya.replace("i", "u")
    
    return prawyaya


def merniH(prawyaya):
    """ 3.4.89 """

    prawyaya = prawyaya.replace("mi", "ni")
    
    return prawyaya


def Afuwwamasya_picca(prawyaya):
    """ 3.4.92 """

    prawyaya = "A" + prawyaya
    
    return prawyaya


def serhyapicca(prawyaya):
    """ 3.4.87 """

    prawyaya = prawyaya.replace("si", "hi")
    
    return prawyaya


def awo_heH(prawyaya):
    """ 6.4.105 """

    prawyaya = "_"
    
    return prawyaya


def AmewaH(prawyaya):
    """ 3.4.90 """

    prawyaya = prawyaya.replace("e", "Am")

    return prawyaya


def savAByAm_vAmO(prawyaya):
    """ 3.4.91 """

    prawyaya = prawyaya.replace("se", "sva")
    prawyaya = prawyaya.replace("Xve", "xvam")

    return prawyaya


def ewe_E(prawyaya):
    """ 3.4.93 """

    prawyaya = prawyaya.replace("e", "E")

    return prawyaya


def lot(XAwu, prawyaya, paxa, lakAra, gaNa):
    """ """ 

    # Add lot conditions
    prawyaya_orig = prawyaya

    # parasmEpaxa - wip, was Ji, sip, Was, Wa, mip, vas, mas
    # Awmanepaxa - wa, AwAm, Ja, WAs, AWAm, Xvam, it, vahi, mahif

    # It is not mentioned in the Paushpi PrakriyA that we 
    # handle iw, but we are doing it as the next steps
    # involve both the original prawyayas and also those 
    # after handling iw. 
    prawyaya = handle_iw(prawyaya)[0]

    # parasmEpaxa - wi, was, Ji, si, Was, Wa, mi, vas mas

    if prawyaya == "Ji":
        # This condition is presented at the end in Paushpi Prakriya 
        # We have inserted it here
        if is_aByaswa(XAwu, gaNa):
            prawyaya = axaByaswAw(prawyaya)
        else:
            prawyaya = JoZnwaH(prawyaya)

    if prawyaya in [ "wi", "anwi", "awi" ]:
        prawyaya = eruH(prawyaya)
    
    if prawyaya == "mi":
        prawyaya = merniH(prawyaya)

    if prawyaya in [ "vas", "mas" ]:
        prawyaya = niwyaM_fiwaH(paxa, prawyaya)
    
    if prawyaya in [ "ni", "va", "ma" ]:
        prawyaya = Afuwwamasya_picca(prawyaya)
    
    # mip is not considered here as it is already handled before
    if prawyaya_orig in [ "was", "Was", "Wa" ]:
        prawyaya = wasWasWamipAM_wAnwanwAmaH(paxa, prawyaya_orig)
    
    if prawyaya == "si":
        prawyaya = serhyapicca(prawyaya)

    if prawyaya == "hi":
        if gaNa in axanwa_gaNa:
            prawyaya = awo_heH(prawyaya)
    
    if prawyaya in [ "wu", "_", "hi" ]:
        prawyaya = prawyaya + "/" + "wAw"
    
    # Awmanepaxa - wa, AwAm, Ja, WAs, AWAm, Xvam, i, vahi, mahi

    # Add logic for tiwa_AwmanepaxAnAM_tere - not provided in 
    # Paushpi Prakriya
    # This is not specified in Paushpi Prakriya but has 
    # to be understood from lat
    if prawyaya in [ "wa", "AwAm", "Ja", "AWAm", "Xvam", "i", "vahi", "mahi" ]:
        prawyaya = tiwa_AwmanepaxAnAM_tere(prawyaya, paxa, lakAra)
    
    if prawyaya in [ "Awe", "AWe" ]:
        if gaNa in axanwa_gaNa:
            prawyaya = Awo_fiwaH(prawyaya, gaNa)
            prawyaya = lopo_vyorvali(prawyaya)
        else:
            pass
        prawyaya = tiwa_AwmanepaxAnAM_tere(prawyaya, paxa, lakAra)
    
    if prawyaya == "WAs":
        prawyaya = WAsaH_se(prawyaya)
    
    if prawyaya == "Je":
        if gaNa in axanwa_gaNa:
            prawyaya = JoZnwaH(prawyaya)
        else:
            prawyaya = AwmanepaxeRvanawaH(prawyaya)
        prawyaya = tiwa_AwmanepaxAnAM_tere(prawyaya, paxa, lakAra)
    
    if prawyaya in [ "we", "iwe", "anwe", "iWe", "awe" ]:
        prawyaya = AmewaH(prawyaya)
    
    if prawyaya_orig in [ "AwAm", "AWAm" ]:
        if gaNa in axanwa_gaNa:
            pass
        else:
            prawyaya = prawyaya_orig

    if prawyaya in [ "se", "Xve" ]:
        prawyaya = savAByAm_vAmO(prawyaya)
    
    if prawyaya in [ "e", "vahe", "mahe" ]:
        prawyaya = ewe_E(prawyaya)
        
    if prawyaya in [ "vahE", "mahE" ]:
        prawyaya = Afuwwamasya_picca(prawyaya)

    return prawyaya


def viXilif(prawyaya, paxa, lakAra, gaNa):
    """ """ 

    # Add viXilif conditions

    # Add conditions for aByaswa rule

    return prawyaya


def prawyaya_Axesa(XAwu, prawyaya, paxa, lakAra, gaNa, vikaraNa):
    """ """ 

    if lakAra == "lat":
        prawyaya = lat(XAwu, prawyaya, paxa, lakAra, gaNa, vikaraNa)
    elif lakAra == "lot":
        prawyaya = lot(XAwu, prawyaya, paxa, lakAra, gaNa)
    elif lakAra == "laf":
        prawyaya = laf(XAwu, prawyaya, paxa, lakAra, gaNa, vikaraNa)
    elif lakAra == "viXilif":
        prawyaya = viXilif(prawyaya, paxa, lakAra, gaNa)
    else:
        pass

    return prawyaya

