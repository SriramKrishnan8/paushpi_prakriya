#!/usr/bin/env python3

import os
import sys

import re


BrASAxi = [ "BrAS", "BlAS", "Bram", "kram", "klam", "wras", "wrut", "laR" ]

def get_res(upasarga, XAwu, vikaranas):
    """ """ 

    res = []
    for vik in vikaranas:
        form1 = (upasarga, XAwu) if upasarga else (XAwu,)
        form = form1 + (vik,) if vik else form1
        
        if vik ==  "_":
            res.append(" + ".join(form))
            form = form1
        
        res.append(" + ".join(form))
    
    return res


def get_vikaraNa(upasarga, XAwu, prawyaya_type, prayoga, gaNa):
    """ Inserting vikaraNa prawyaya according to conditions """
    
    vikaraNa = []
    if prawyaya_type == "sArvaXAwuka":
        if prayoga in [ "karmaNi", "BAve" ]:
            # sArvaXAwuke yak (3.1.67)
            vikaraNa.append("yak")
        else:
            # if XAwu in BrASAxi:
            #     # vA BrASaBlASaBramukramuklamuwrasiwrutilaRaH (3.1.70) 
            #     vikaraNa.append("Syan")
            #     vikaraNa.append("Sap")
            # elif upasarga == "_" and XAwu == "yas":
            #     if upasarga == "_":
            #         # yasoZnupasargAw (3.1.72)
            #         vikaraNa.append("Syan")
            #         vikaraNa.append("Sap")
            #     elif upasarga == "sam":
            #         # saMyasaSca (3.1.73)
            #         vikaraNa.append("Syan")
            #         vikaraNa.append("Sap")
            # elif gaNa == "xivAxi":
            #     # xivAxiByaH Syan (3.1.69)
            #     vikaraNa.append("Syan")
                
            if gaNa == "axAxi":
                # karwari Sap (3.1.68)
                vikaraNa.append("Sap")
                # axipraBqwiByaH SapaH (2.4.72)
                vikaraNa.append("luk")
                vikaraNa.append("_")
            
            if gaNa == "juhowyAxi":
                # karwari Sap (3.1.68)
                vikaraNa.append("Sap")
                # juhowyAxiByaH SluH (2.4.75)
                vikaraNa.append("Slu")
                vikaraNa.append("_")
            
            if gaNa == "xivAxi":
                vikaraNa.append("Syan")
            
            if XAwu in BrASAxi:
                # vA BrASaBlASaBramukramuklamuwrasiwrutilaRaH (3.1.70) 
                if "Syan" not in vikaraNa:
                    vikaraNa.append("Syan")
                if "Sap" not in vikaraNa:
                    vikaraNa.append("Sap")
            
            if XAwu == "yas":
                if upasarga == "":
                    # yasoZnupasargAw (3.1.72)
                    vikaraNa.append("Sap")
                elif upasarga == "sam":
                    # saMyasaSca (3.1.73)
                    vikaraNa.append("Sap")
                else:
                    pass
            
            if gaNa == "svAxi":
                # svAxiByaH SnuH (3.1.73)
                vikaraNa.append("Snu")
            
            if gaNa == "wuxAxi":
                # wuxAxiByaH SaH (3.1.77)
                vikaraNa.append("Sa")
            
            if gaNa == "ruXAxi":
                # ruXAxiByaH Snam (3.1.78)
                vikaraNa.append("Snam")
            
            if gaNa == "wanAxi":
                # wanAxikqFByaH uH (3.1.79)
                vikaraNa.append("u")
            
            if gaNa == "kryAxi":
                # kryAxiByaH SnA (3.1.81)
                vikaraNa.append("SnA")
            
            if XAwu in [ "swamB", "swunB", "skanB", "skunB", "skuF" ]:
                # swamBaswunBaskanBaskunBaskuFByaH SnuSca (3.1.70) 
                vikaraNa.append("Snu")
            
            if not vikaraNa:
                # karwari Sap (3.1.68)
                vikaraNa.append("Sap")
    else:
        # ArXaXAwuka prawyaye pare
        vikaraNa.append("")
    
    return vikaraNa


def insert_vikaraNa(upasarga, XAwu, prawyaya_type, prayoga, gaNa):
    """ """ 

    vikaraNa = get_vikaraNa(upasarga, XAwu, prawyaya_type, prayoga, gaNa)
    res = get_res(upasarga, XAwu, vikaraNa)
    
    # eqs = [ upasarga + " + " + XAwu + " + " + vik for vik in vikaraNa ]
    # mod_eqs = [ x.strip() for x in eqs ]

    return res

