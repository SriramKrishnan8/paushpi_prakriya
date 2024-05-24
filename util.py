#!/usr/bin/env python3

#from saFjFA.prawyAhAra_saFjFA import get_letters

mAheSvara_list_orig = [
    "a", "i", "u", "N!", 
    "q", "L", "k!", 
    "e" ,"o", "f!", 
    "E", "O", "c!", 
    "ha", "ya", "va", "ra", "t!", 
    "la", "N!", 
    "fa", "ma", "Fa", "Na", "na", "m!", 
    "Ja", "Ba", "F!", 
    "Ga", "Da", "Xa", "R!", 
    "ja", "ba", "ga", "da", "xa", "S!", 
    "Ka", "Pa", "Ca", "Ta", "Wa", "ca", "ta", "wa", "v!", 
    "ka", "pa", "y!", 
    "Sa", "Ra", "sa", "r!", 
    "ha", "l!", 
]

mAheSvara_list = [
    "a", "i", "u", "N!", 
    "q", "L", "k!", 
    "e" ,"o", "f!", 
    "E", "O", "c!", 
    "h", "y", "v", "r", "t!", 
    "l", "N!", 
    "f", "m", "F", "N", "n", "m!", 
    "J", "B", "F!", 
    "G", "D", "X", "R!", 
    "j", "b", "g", "d", "x", "S!", 
    "K", "P", "C", "T", "W", "c", "t", "w", "v!", 
    "k", "p", "y!", 
    "S", "R", "s", "r!", 
    "h", "l!", 
]

ac = [ 
    "a", "A", "i", "I", "u", "U", 
    "q", "Q", "L", 
    "e", "o", 
    "E", "O" 
]
hal = [ 
    "h", "y", "v", "r", 
    "l", 
    "f", "m", "F", "N", "n", 
    "J", "B", 
    "G", "D", "X", 
    "j", "b", "g", "d", "x", 
    "K", "P", "C", "T", "W", "c", "t", "w",
    "k", "p", 
    "S", "R", "s"
]

all_prawyAhAras_list = [
    "aN", "ak", "ik", "uk", "ef", "ac", "ic", "ec", "Ec",
    "at", "aN", "iN", "yaN", "am", "Fam", "fam", "yaF",
    "BaR", "JaR", "aS", "haS", "vaS", "jaS", "JaS", "baS",
    "Cav", "yay", "may", "Jay", "Kay", "cay", "yar", "Jar",
    "Kar", "car", "Sar", "al", "hal", "val", "ral", "Jal", "Sal",
]

anunAsika = "z"
ka_varga = [ "k", "K", "g", "G", "f" ]
ca_varga = [ "c", "C", "j", "J", "F" ]
ta_varga = [ "t", "T", "d", "D", "N" ]
wa_varga = [ "w", "W", "x", "X", "n" ]
pa_varga = [ "p", "P", "b", "B", "m" ]


guNa = [ "a", "e", "o" ]
vqxXi = [ "A", "E", "O" ]
Gu = [ "duxAF", "xAN", "xo", "xef", "Xet", "duXAF" ]

sarvanAma = [
    "sarva", "viSva", "uBa", "uBaya", "dawara", "dawama", "iwara", "anya", 
    "anyawara", "wvaw", "wva", "nema", "sama", "sima", 
    "wyax", "wax", "yax", "ewax", "ixam", "axas", "eka", "xvi", "yuRmax", 
    "asmax", "Bavawu", "kim", 
    "pUrva", "para", "avara", "xakRiNa", "uwwara", "apara", "aXara", 
    "sva", "anwara", 
]

avyaya = [
    
]


XAwus_list = [ 
    "gamLz", "dukqF", "vaxiz", "FimixAz", "tunaxIz", "FikRvixAz", "tukRu",
    "tudu", "dulaBazR", "dupacazR", "uzCqxizr", "Ihaz", 
    "uzXrasaz", "ozpyAyoz", "ozladiz", "ozvrascUz", "tuozsPUrjAz",
    "kurxaz", "Kurxaz", "gurxaz", "vaxi", "Naxi", "narxaz", "nAWqz", "nAt", 
    "nQ", "Nam", "Rvaxaz", "RTA", "RNA", "RvARka", "RTivu", "svaxaz", "Rmif", 
    "RUxaz", "RiXaz", "RiF", "sWA", "swu", 
]
all_prawyayas = [ 
    "RAkan", "Rtran", "Rvun",
    "Ra", "Rac", "Rafgavac", "Rikan", "ReNyan", "Rkan", "Rtarac", "RTac", 
    "RTan", "RTal", "RPak", "Ryaf", "RyaF", "RPa",
    "kwvA", "wumun",
    "Sap", "Syan", "gsnu", "Kyun", "KiRNuc", "fi", "GaF", 
    "suz", "O", "jas", "am", "Ot", "Sas", "tA",
    "wip", "was", "Ji", "mahi", "tAp",
    "wasil", "lac", "Gan", "Sas", "ka", "Ka", "gmini", 
    "Namul", "Sawq", "SAnac", "Snam", "lyut", "kyac",
    "Nic", 
]

wip_mas = [
    "wip", "was", "Ji", "sip", "Was", "Wa", "mip", "vas", "mas", 
]

wa_mahif = [
    "wa", "AwAm", "Ja", "WAs", "AWAm", "Xvam", "it", "vahi", "mahif", 
]

wif_prawyayas = wip_mas + wa_mahif

parasmEpaxa = wip_mas + [ "Sawq", "kvasu" ]
Awmanepaxa = wa_mahif + [ "SAnac", "kAnac" ]

sup_prawyayas = [
    "su", "O", "jas", "am", "Ot", "Sas", "tA", "ByAm", "Bis", 
    "fe", "ByAm", "Byas", "fasi", "ByAm", "Byas", 
    "fas", "os", "Am", "fi", "os", "sup", 
]

viBakwi_saFjFA = sup_prawyayas + wif_prawyayas

niRTA = [ "kwa", "kwavawu" ]

R_prawyayas = [
    "RAkan", "Rtran", "Rvun",
    "Ra", "Rac", "Rafgavac", "Rikan", "ReNyan", "Rkan", "Rtarac", "RTac", 
    "RTan", "RTal", "RPak", "Ryaf", "RyaF", "RPa",
]
waxXiwa_prawyayas = [
    "wasil", "lac", "Gan", "Sas", "ka", "Ka", "gmini", 
]

sArvaXAwuka_prawyaya = [
    "mi", "vaH", "va", "ma", "vahi", "mahi",
]



cAxi = [ "ca", "vA", "ha", "aha", "eva", "evam", "nUnam", "SaSvaw", "yugapaw",
    "BUyas", "sUpaw", "kUpaw",
]

asawwva_cAxi = cAxi

prAxi = [
    "pra", "parA", "apa", "sam", "anu", "ava", 
    "nis", "nir", "xus", "xur", "vi", "Af", "ni", 
    "aXi", "api", "awi", "su", "uw", "aBi", 
    "prawi", "pari", "upa", 
]

asawwva_prAxi = prAxi


UryAxi_gaNa = [ 
    "UrI", "urarI", "wanWI", "wAlI", "AwwAlI", "vewAlI", "XUlI", "XUsa", 
    "SakalA", "saMSakalA", "XvaMsakalA", "BraMsakalA", "guluguXA", "sajUs", 
    "Pala", "PalI", "viklI", "AklI", "AloRTI", "kevAlI", "kevAsI", "sevAsI", 
    "paryAlI", "SevAlI", "varRAlI", "awyUmaSA", "maSmaSA", "masmasA", 
    "masamasA", "ORat", "SrORat", "vORat", "vaRat", "svAhA", "svaXA", 
    "vanXA", "prAxus", "Sraw", "Avis" 
]



kaNTa = [ "a", "A", "h", "H" ] + ka_varga
wAlu = [ "i", "I", "y", "S" ] + ca_varga
mUrXA = [ "q", "Q", "r", "R" ] + ta_varga
xanwa = [ "L", "l", "s" ] + wa_varga
oRTa = [ "u", "U" ] + pa_varga
nAsikA = [ "F", "m", "f", "N", "n", "M" ]
kaNTa_wAlu = [ "e", "E" ]
kaNTa_oRTa = [ "o", "O" ]
xanwa_oRTa = [ "v" ]

# bAhya_prayawna
#vivAra = get_letters("Kar")[0]
#SvAsa = get_letters("Kar")[0]
#aGoRa = get_letters("Kar")[0]
#saMvAra = get_letters("haS")[0]
#nAxa = get_letters("haS")[0]
#GoRa = get_letters("haS")[0]
#alpapRANa = ka_varga[0::2] + ca_varga[0::2] + ta_varga[0::2] + wa_varga[0::2] \
#    + pa_varga[0::2] + get_letters("yaN")[0]
#mahAprANa = ka_varga[1::2] + ca_varga[1::2] + ta_varga[1::2] + wa_varga[1::2] \
#    + pa_varga[1::2] + get_letters("Sal")[0]

# AByanwara_prayawna
#spqRta = ka_varga + ca_varga + ta_varga + wa_varga + pa_varga
#IRaw_spqRta = get_letters("yat")[0]
#IRax_vivqwa = [ "S", "R", "s" , "h" ]
#vivqwa = ac[1:]
#saMvqwa = [ "a" ]

#uxAwwa = ac
#anuxAwwa = ac
#svariwa = ac

qkAra_XAwu = [
    "qcCa", "Q", "qX", "QN", "qwi", "q"
]
