#!/usr/bin/env python3

import os
import sys

import re

import argparse

from saFjFA.iw_saFjFA import print_iw
from saFjFA.prawyAhAra_saFjFA import print_prawyAhAra
from saFjFA.saFjFA import ti
from sanXi.sanXi import sanXi_op
from preprocess.preprocess import XAwu_operations, paxanirNaya_viXi
from upAfga.vikaraNa import get_vikaraNa


def test_iw():
    """ For internal testing
    """
    
    iw_examples = [
        "suz", "Bavawuz", "gamLz", "dupacazR", "BU", "tuozSvi", "lazN", 
        "vaxiz", "dukqF", "kwvA", "wumun", "Sap", "NIF", "Bixir", "Cixizr", 
        "FimixAz", "tunaxIz", "RAkan", "RPak", "RTac", "RPa", "jas", "tA", 
        "Sap", "Syan", "gsnu", "Kyun", "Snam", "Sawq", "SAnac", "lyut", 
        "kyac", "KiRNuc", "fi", "GaF", "wasil", "lac", "gmini", "Gan", "Sas", 
        "ka", "Ka", "Namul", "uzCqxizr", "Ihaz", "uzXrasaz", "ozpyAyoz", 
        "ozladiz", "ozvrascUz", "tuozsPUrjAz"
    ]
    
    for iw_ex in iw_examples:
        print_iw(iw_ex)
    

def test_prawyAhAra():
    """ All available prawyAhAras are enlisted here
    """
    
    from util import all_prawyAhAras_list
    
    for pr in all_prawyAhAras_list:
        print_prawyAhAra(pr)
        

def print_ti(term):
    """ """
    
    ti_term, ti_start_index = ti(term)
    print(term + " -> " + str(ti_term) + ": " + str(ti_start_index))


def test_ti():
    """ """
    
    ti_examples = [
        "suz", "Bavawuz", "gamLz", "dupacazR", "BU", "tuozSvi", "lazN", 
        "vaxiz", "dukqF", "kwvA", "wumun", "Sap", "NIF", "Bixir", "Cixizr", 
        "FimixAz", "tunaxIz", "RAkan", "RPak", "RTac", "RPa", "jas", "tA", 
        "Sap",
    ]
    
    for pr in ti_examples:
        print_ti(pr)


def print_upaXA(term):
    """ """
    
    from saFjFA.saFjFA import upaXA
    
    upaXA_str, upaXA_ind, upaXA_type = upaXA(term)
    print(term + " -> " + upaXA_str + "," + str(upaXA_ind) + "," + upaXA_type)


def test_upaXA():
    """ """
    
    examples = [
        "suz", "Bavawuz", "gamLz", "dupacazR", "BU", "tuozSvi", "lazN", 
        "vaxiz", "dukqF", "kwvA", "wumun", "Sap", "NIF", "Bixir", "Cixizr", 
        "FimixAz", "tunaxIz", "RAkan", "RPak", "RTac", "RPa", "jas", "tA", 
        "Sap",
    ]
    
    for pr in examples:
        print_upaXA(pr)
        

def test_sandhi(first, second):
    """ """
    
    res = sanXi_op(first, second)
    print(first + " + " + second + " -> " + res)


def test_sandhi_examples():
    """ """
    
    examples_ac = [
        ("prawi", "ekaH"), ("maXu", "ariH"), ("XAwq", "aMSaH"), ("L", "AkqwiH"),
        ("ne", "a"), ("Bo", "a"), ("XyE", "a"), ("pO", "a"),
        ("nene", "Ava"), ("nene", "Ani"), ("cino", "e"), ("cino", "Ani"),
        ("na", "api"), ("Bava", "Ani"), ("ramA", "aswi"),
        ("muni", "ISaH"), ("paTawi", "ixam"), ("gOrI", "iyam"),
        ("laGu", "UrmiH"), ("BAnu", "uxayaH"), ("SvaSrU", "UkAraH"),
        ("howq", "qkAraH"), 
        ("sura", "ISaH"), ("waWA", "iwi"), ("sUrya", "uxayaH"), ("gafgA", "uxakam"),
        ("mahA", "qRiH"), ("wava", "LkAraH"),
        ("mahA", "ORaXam"), ("gafgA", "oGaH"), ("kqRNa", "ekawvam"), ("eXa", "E"),
        ("naya", "mi"), ("naya", "vaH"), ("anaya", "va"), ("anaya", "ma"), 
        ("anaya", "vahi"), ("anaya", "mahi"), 
        ("viSNU", "imO"), ("gafge", "amU"), ("harI", "ewO"), 
        ("rAma", "am"), ("muni", "am"), ("guru", "am"), 
        ("hare", "ava"), ("viSNo", "ava"), 
    ]
    
    examples_hal = [
        ("haris", "Sewe"), ("xus", "cariwaH"), ("saw", "ciw"), ("uw", "cAraNam"), 
        ("ux", "jvalaH"), ("sax", "janaH"), ("yAc", "nA"), ("SArfgin", "jayaH"), 
        ("lolot", "wi"), ("xuR", "taH"), ("waw", "tIkA"), ("peR", "wA"), 
        ("rAmas", "RaRTaH"), ("viR", "nuH"), ("ux", "dInaH"), ("kqR", "naH"), 
        ("ne", "syawi"), ("ho", "syawi"), ("Sak", "syawi"), ("pA", "syawi"), 
        ("aSASak", ""), ("acAkaK", ""), ("arArag", ""), ("ajAjaG", ""), 
        ("arArat", ""), ("aloloT", ""), ("acAkad", ""), ("avAvaD", ""), 
        ("ayAyaw", ""), ("avAvyaW", ""), ("arArax", ""), ("arAraX", ""), 
        ("alAlap", ""), ("arAraP", ""), ("acAkab", ""), ("alAlaB", ""), 
        ("acAkAS", ""), ("alAlaR", ""), 
        ("xuG", ""), ("boX", "sya"), ("buX", "Xvam"), 
        ("aBiws", "wa"), 
    ]
    
    for first, second in examples_hal:
        res = sanXi_op(first, second)
        print(first + " + " + second + " -> " + ",".join(res))


def print_XAwu_changes(XAwu):
    """ """
    
    print("\nmUla_XAwu: " + XAwu)
    raw_XAwu = XAwu_operations(XAwu)
    print("XAwu: " + raw_XAwu)


def test_XAwu_changes():
    """ """
    
    from util import XAwus_list
    
    for XAwu in XAwus_list:
        print_XAwu_changes(XAwu)


def print_paxa(XAwu):
    """ """
    
    paxa = paxanirNaya_viXi(XAwu)
    print(XAwu + ": " + paxa)


def test_paxa():
    """ """
    
    temp_Xawus_list = [ "pac", "yAc", "eX", "As", "paT", "gam" ]

    for XAwu in temp_Xawus_list:
        print_paxa(XAwu)


def print_vikaraNa(upasarga, XAwu, prawyaya_type, prayoga, gaNa):
    """ """ 

    res_lst = get_vikaraNa(upasarga, XAwu, prawyaya_type, prayoga, gaNa)
    upasarga = upasarga or "-"
    print(upasarga, XAwu, prawyaya_type, prayoga, gaNa)
    print("\n".join(res_lst))


def test_vikaraNa():
    """ """
    
    temp_input_list = [ 
        ("", "pac", "sArvaXAwuka", "karwari", "BvAxi"),
        ("", "pac", "sArvaXAwuka", "karmaNi", "BvAxi"),
        ("", "pac", "sArvaXAwuka", "BAve", "BvAxi"),
        ("", "pac", "ArXaXAwuka", "karwari", "BvAxi"),
        ("", "pac", "ArXaXAwuka", "karmaNi", "BvAxi"),
        ("", "pac", "ArXaXAwuka", "BAve", "BvAxi"),
        ("vi", "wan", "sArvaXAwuka", "karwari", "wanAxi"),
        ("vi", "wan", "sArvaXAwuka", "karmaNi", "wanAxi"),
        ("vi", "wan", "sArvaXAwuka", "BAve", "wanAxi"),
        ("", "As", "sArvaXAwuka", "karwari", "axAxi"),
        ("", "hu", "sArvaXAwuka", "karwari", "juhowyAxi"),
        ("", "xiv", "sArvaXAwuka", "karwari", "xivAxi"),
        ("", "wux", "sArvaXAwuka", "karwari", "wuxAxi"),
        ("", "ruX", "sArvaXAwuka", "karwari", "ruXAxi"),
        ("", "krI", "sArvaXAwuka", "karwari", "kryAxi"),
        ("", "cur", "sArvaXAwuka", "karwari", "curAxi"),
        ("", "yas", "sArvaXAwuka", "karwari", "xivAxi"),
        ("sam", "yas", "sArvaXAwuka", "karwari", "xivAxi"),
        ("", "swamB", "sArvaXAwuka", "karwari", "wuxAxi"),
        ("", "Bram", "sArvaXAwuka", "karwari", "BvAxi"),
    ]

    for input_ in temp_input_list:
        print_vikaraNa(*input_)


def main():
    """ """
    
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", "--type", default="iw", 
        choices=[
            "iw", "prawyAhAra", "ti", "upaXA", "sanXi",
            "XAwu_changes", "paxa", "vikaraNa", 
        ],
        help="what to test?"
    )
    parser.add_argument(
        "-o", "--own", type=str,
        help="own example"
    )
    parser.add_argument(
        "-f", "--first", type=str,
        help="first word"
    )
    parser.add_argument(
        "-s", "--second", type=str,
        help="second word"
    )

    args = parser.parse_args()

    if args.type == "iw":
        if args.own:
            print_iw(args.own)
        else:
            test_iw()
    elif args.type == "prawyAhAra":
        if args.own:
            print_prawyAhAra(args.own)
        else:
            test_prawyAhAra()
    elif args.type == "ti":
        if args.own:
            print_ti(args.own)
        else:
            test_ti()
    elif args.type == "upaXA":
        if args.own:
            print_upaXA(args.own)
        else:
            test_upaXA()
    elif args.type == "sanXi":
        if args.first or args.second:
            test_sandhi(args.first, args.second)
#            print("Please provide the two terms to be sandhied")
        else:
            test_sandhi_examples()
    elif args.type == "XAwu_changes":
        if args.own:
            print_XAwu_changes(args.own)
        else:
            test_XAwu_changes()
    elif args.type == "paxa":
        if args.own:
            print_paxa(args.own)
        else:
            test_paxa()
    elif args.type == "vikaraNa":
        test_vikaraNa()


if __name__ == "__main__":
    main()
