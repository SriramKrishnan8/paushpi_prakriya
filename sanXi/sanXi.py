#!/usr/bin/env python3

import os
import sys

import re

from saFjFA.prawyAhAra_saFjFA import get_letters
from saFjFA.savarNa import get_savarNa
from saFjFA.pragqhya_saFjFA import is_pragqhya
from saFjFA.saFjFA import is_pluwa, is_ekAc

from util import sArvaXAwuka_prawyayas, wa_varga, ca_varga, ta_varga, ka_varga


ac_sandhi = [
    
]


def ac_op(first, second):
    """ """
    
    res = first + second
    
    # iko yaNaci (6.1.77)
    ik = get_letters("ik")[0]
    ac = get_letters("ac")[0]
    yaN = {
        "i" : "y", "I" : "y", 
        "u" : "v", "U" : "v", 
        "q" : "r", "Q" : "r",
        "L" : "l"
    }
    
    # ecoZyavAyAvaH (6.1.78)
    ec = get_letters("ec")[0]
    ayavAyAv = {
        "e" : "ay", "o" : "av", 
        "E" : "Ay", "O" : "Av", 
    }
    
    # akaH savarNe xIrGaH (6.1.101)
    ak = get_letters("ak")[0]
    savarNa_xIrGa = {
        "a" : "A", "i" : "I", "u" : "U", "q" : "Q", 
        "A" : "A", "I" : "I", "U" : "U", "Q" : "Q", 
    }
    
    # AxguNaH (6.1.87)
    guNa = {
        "i" : "e", "I" : "e",
        "u" : "o", "U" : "o",
        "q" : "ar", "Q" : "ar",
        "L" : "al",
    }
    
    # vqxXireci (6.1.88)
    vqxXi = {
        "e" : "E", "E" : "E",
        "o" : "O", "O" : "O",
    }
    
    # ewyeXawyUTsu (6.1.89)
    # requires first to be ewi or eXawi or UT
    # some say it can be from iN-XAwu or eX-XAwu or UT-Sabxa
    # requires morphological analyses in this case
    # hence not implemented now
    
    # upasargAxqwi XAwoH (6.1.91)
    # first should be "a"-ending and second should have q-Axi XAwu
    # requires morphological analyses in this case
    # hence not implemented now
    
    # AtaSca (6.1.90)
    # requires XAwu to be ajAxi and lakAra to be laf
    
    # efi pararUpam (6.1.94)
    # requires first to be a-ending upasarga
    # and second from XAwu starting with e and o
    
    # awo guNe (6.1.97)
    # first should be a-ending and not be a word, second in a, e, o
    
    # ami pUrvaH (6.1.107)
    
    # efaH paxAnwAxawi (6.1.109)
    # first should be paxa and ending in ef and 
    # second should start with a
    ef = get_letters("ef")[0]
    
    # pluwapragqhyA aci niwyam (6.1.125)
    # pragqhya requires morphological analyses
    
    # awo xIrGO yaFi (7.3.101)
    # first should be a-ending afga
    
    f = first[-1]
    f_2 = first[-2:]
    s = second[0] if second else ""
    
    if f in ik and s in ac:
        res = first[:-1] + yaN.get(f, f) + second 
    if f in ec and second[0] in ac:
        res = first[:-1] + ayavAyAv.get(f, f) + second 
    if f in ak and second[0] in ac and second[0] in get_savarNa(f):
        res = first[:-1] + savarNa_xIrGa.get(f, f) + second[1:]
    if f in [ "a", "A" ] and s in ik:
        res = first[:-1] + guNa.get(s, s) + second[1:]
    if f in [ "a", "A" ] and s in ec:
        res = first[:-1] + vqxXi.get(s, s) + second[1:]
    # 6.1.89
    # 6.1.91
    # 6.1.90
#    if f == "A" and s in ik: # also check if laf-lakAra and XAwu is ajAxi
#        res = first[:-1] + vqxXi.get(s, s) + second[1:]
    # 6.1.94
    # 6.1.97
    if f in ak and second == "am":
        res = first + "m"
    if f in ef and s == "a": # also check if first is paxa or not
        res = first + "Z" + second[1:]
    if (is_pragqhya(first) or is_pluwa(first)) and s in ac:
        res = first + " " + second
    if f == "a" and second in sArvaXAwuka_prawyayas:
        res = first[:-1] + "A" + second
    
    return [ res ]


def swoH_ScunA_ScuH(first, second):
    """ swoH ScunA ScuH (8.4.40) """ 
    
    res = ""
    
    # swoH ScunA ScuH (8.4.40)
    Scu_for_swu = {
        "s" : "S", "w" : "c", "W" : "C",
        "x" : "j", "X" : "J", "n" : "F",
    }
    if first[-1] in (wa_varga + [ "s" ]) and second and second[0] in (ca_varga + [ "S" ]):
        res = first[:-1] + Scu_for_swu.get(first[-1], first[-1]) + second
    elif first[-1] in (ca_varga + [ "S" ]) and second and second[0] in (wa_varga + [ "s" ]):
        res = first + Scu_for_swu.get(second[0], second[0]) + second[1:]
    
    return res


def Rtuna_RtuH(first, second):
    """ Rtuna RtuH (8.4.41) """
    
    res = ""
    
    # Rtuna RtuH (8.4.41)
    Scu_for_Rtu = {
        "s" : "R", "w" : "t", "W" : "T",
        "x" : "d", "X" : "D", "n" : "N",
    }
    if first[-1] in (wa_varga + [ "s" ]) and second and second[0] in (ta_varga + [ "R" ]):
        res = first[:-1] + Scu_for_Rtu.get(first[:-1], first[:-1]) + second
    elif first[-1] in (ta_varga + [ "R" ]) and second and second[0] in (wa_varga + [ "s" ]):
        res = first + Scu_for_Rtu.get(second[0], second[0]) + second[1:]
        
    return res


def AxeSaprawyayayoH(first, second):
    """ """
    
    res = ""
    
    # AxeSaprawyayayoH (8.3.59)
    # should check AxeSa or prawyaya
    iN = get_letters("iN")[1]
    if first[-1] in iN + ka_varga and second.startswith("s"):
        res = first + "R" + second[1:]
        
    return res
    

def jalAM_jaSoZnwe(first, second):
    """ """
    
    res = ""
    
    # jalAM jaSoZnwe (8.2.39)
    Jal = get_letters("Jal")[0]
    jaS_for_Jal = {
        "k" : "g", "K" : "g", "g" : "g", "G" : "g",
        "c" : "j", "C" : "j", "j" : "j", "J" : "j",
        "t" : "d", "T" : "d", "d" : "d", "D" : "d",
        "w" : "x", "W" : "x", "x" : "x", "X" : "x",
        "p" : "b", "P" : "b", "b" : "b", "B" : "b",
        "R" : "d", "s" : "x",
        "S" : "d", # Here due to the sUwra vraScaBrasj... (8.2.36),
        # S becomes R, and because of RNAnwAH Rat, it becomes d
    }
    
    if first[-1] in Jal and second == "":
        res = first[:-1] + jaS_for_Jal.get(first[-1], first[-1])
    
    return res


def vAZvasAne(first, second):
    """ """
    
    res = ""
    
    # vAZvasAne (8.2.56)
    
    Jal = get_letters("Jal")[0]
    
    # After jaSwva, carwva is done and hence a direct map 
    # from Jal to car is given here  
    car_for_Jal = {
        "k" : "k", "K" : "k", "g" : "k", "G" : "k",
        "c" : "c", "C" : "k", "j" : "k", "J" : "c",
        "t" : "t", "T" : "t", "d" : "t", "D" : "t",
        "w" : "w", "W" : "w", "x" : "w", "X" : "w",
        "p" : "p", "P" : "p", "b" : "p", "B" : "p",
        "R" : "t", "s" : "w",
        "S" : "t", # Here due to the sUwra vraScaBrasj... (8.2.36),
        # S becomes R, and because of RNAnwAH Rat, it becomes d
    }
    
    if first[-1] in Jal and second == "":
        res = first[:-1] + car_for_Jal.get(first[-1], first[-1])
        
    return res
    

def ekAco_baSo_BaR_JaSanwasya_sXvoH(first, second):
    """ """
    
    res = ""
    
    # ekAco baSo BaR JaSanwasya sXvoH (8.2.37)
    JaR = get_letters("JaR")[0]
    baS = get_letters("baS")[0]
    if is_ekAc(first) and first[-1] in JaR and any([x in baS for x in first]):
        if second == "" or second[0] == "s" or second.startswith("Xva"): # Add if paxAnwa
            new_first = first[:]
            res = new_first.replace("b", "B")
            res = res.replace("g", "G")
            res = res.replace("d", "D")
            res = res.replace("x", "X")
            
            res = res + " " + second
            
            
    return res
    

def Xi_ca(first, second):
    """ """
    
    res = ""
    
    # Xi ca (8.2.25)
    if first[-1] == "s" and second[0] == "X":
        res = first[:-1] + second
        
    return res
    

def Jalo_Jali(first, second):
    """ """
    
    res = ""
    
    Jal = get_letters("Jal")[0]
    # Jalo Jali (8.2.26)
    if first[-2] in Jal and first[-1] == "s" and second[0] in Jal:
        res = first[:-1] + second
    
    return res


def sasajuRo_ruH(first, second):
    """ sasajuRo ruH (8.2.66) """
    
    res = ""
    
    # sasajuRo ruH (8.2.66)
    
    # how to check if first is paxa?
    
    if first[-1] == "s" and second == "":
        res = first[:-1] + "r"
    else:
        res = first + " " + second
        
    return res.strip()


def KaravasAnayorvisarjanIyaH(first, second):
    """ """
    
    res = ""
    
    # KaravasAnayorvisarjanIyaH (8.3.15)
    
    Kar = get_letters("Kar")[0]
    if first[-1] == "r" and (second == "" or second[0] in Kar):
        res = first[:-1] + "H " + second
    else:
        res = first + " " + second
    
    return res.strip()
    

def haSi_ca(first, second):
    """ """
    
    res = ""
    
    # haSi ca (6.1.114)
    
    haS = get_letters("haS")[0]
    if first.endswith("ar") and second[0] in haS:
        res = first[:-2] + "o " + second
    
    return res
    

jaS_for_Jal = {
    "k" : "g", "K" : "g", "g" : "g", "G" : "g",
    "c" : "j", "C" : "j", "j" : "j", "J" : "j",
    "t" : "d", "T" : "d", "d" : "d", "D" : "d",
    "w" : "x", "W" : "x", "x" : "x", "X" : "x",
    "p" : "b", "P" : "b", "b" : "b", "B" : "b",
    "R" : "d", "s" : "x",
    "S" : "j", # Here due to the sUwra vraScaBrasj... (8.2.36),
    # S becomes R, and because of RNAnwAH Rat, it becomes d
}


def JalAM_jaS_JaSi(first, second):
    """ """ 
    
    res = ""
    
    Jal = get_letters("Jal")[0]
    JaS = get_letters("JaS")[0]
    
    if first[-1] in Jal and second and second[0] in JaS:
        res = first[:-1] + jaS_for_Jal.get(first[-1], first[-1]) + second
    
    return res


def Kari_ca(first, second):
    """ """ 
    
    res = ""
    
    Jal = get_letters("Jal")[0]
    Kar = get_letters("Kar")[0]
    # Kari ca (8.4.55)
    car_for_Jal = {
        "k" : "k", "K" : "k", "g" : "k", "G" : "k",
        "c" : "c", "C" : "k", "j" : "k", "J" : "c",
        "t" : "t", "T" : "t", "d" : "t", "D" : "t",
        "w" : "w", "W" : "w", "x" : "w", "X" : "w",
        "p" : "p", "P" : "p", "b" : "p", "B" : "p",
        "R" : "R", "s" : "s",
        "S" : "S", # Here due to the sUwra vraScaBrasj... (8.2.36),
        # S becomes R, and because of RNAnwAH Rat, it becomes d
    }
    
    
    if first[-1] in Jal and second and second[0] in Kar:
        res = first[:-1] + car_for_Jal.get(first[-1], first[-1]) + second
    
    return res
    

def JaRaswaWoZrXoZXaH(first, second):
    """ """ 
    
    res = ""
    
    # JaRaswaWoZrXoZXaH (8.2.40)
    JaR = get_letters("JaR")[0]
    # add condition the XA XAwu should not be included here.  
    if first[-1] in JaR and second and second[0] in [ "w", "W" ]:
        res = first[:-1] + jaS_for_Jal.get(first[-1], first[-1]) + "X" + second[1:]
        
    return res
    

def RaDoH_kaH_si(first, second):
    """ """
    
    res = ""
    
    # RaDoH kaH si (8.2.61)
    
    if first[-1] == "R" and second and second[0] == "s":
        res = first[:-1] + "k" + second
        
    return res
    

def saH_syArXaXAwuke(first, second):
    """ """
    
    res = ""
    
    # saH syArXaXAwuke (7.4.49)
    
    if first[-1] == "s" and second[0] == "s" and second not in sArvaXAwuka_prawyayas:
        res = first[:-1] + "w" + second
    
    return res
    

def hal_op(first, second):
    """ """ 
    
    res = first + second
    
    f = first[-1]
    f_2 = first[-2:]
    s = second[0] if second else ""
    
    results = []
    
    # Scuwva
    results.append(swoH_ScunA_ScuH(first, second))
    
    # Rtuwva
    results.append(Rtuna_RtuH(first, second))
    
    # Rawva
    results.append(AxeSaprawyayayoH(first, second))
    
    # Refer RopaxeSa XAwu Pg. 30
    
    # Nawva
    
    # jaSwva
    results.append(jalAM_jaSoZnwe(first, second))
    # carwva
    results.append(vAZvasAne(first, second))
    
    # BaRwva
    results.append(ekAco_baSo_BaR_JaSanwasya_sXvoH(first, second))
    
    # salopa
    results.append(Xi_ca(first, second))
    results.append(Jalo_Jali(first, second))
    # hrasvAxafgAw (8.2.27)
    # This and the previous sUwra require three terms.  
    # Check how to handle them.
    
    # ruwva, visarga
    results.append(sasajuRo_ruH(first, second))
    results.append(KaravasAnayorvisarjanIyaH(first, second))
    
    # the above sUwras are applied only at the end
    # -----------------
    
    # uwva
    results.append(haSi_ca(first, second))
    
    # apaxAnwa jaSwva
    results.append(JalAM_jaS_JaSi(first, second))
    
    # carwva
    results.append(Kari_ca(first, second))
    results.append(JaRaswaWoZrXoZXaH(first, second))
    results.append(RaDoH_kaH_si(first, second))
    results.append(saH_syArXaXAwuke(first, second))
    
    # 
    
    return results


def sanXi_op(first, second):
    """ """
    
    results = []
    results += ac_op(first, second)
    results += hal_op(first, second)
    
    # All Sandhi operations go here
    
    return list(set(results))


def terminal_sandhi(term):
    """ """ 

    res = sasajuRo_ruH(term, "")
    res = KaravasAnayorvisarjanIyaH(res, "")

    return res