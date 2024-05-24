#!/usr/bin/env python3

import os
import sys

import re

from util import all_prawyAhAras_list, mAheSvara_list


def add_xIrGa(letters_lst):
    """ Returns an updated list where xIrGa of the first three
        vowels are inserted
    """
    
    xIrGa_dict = {
        "a" : "A", "i" : "I", "u" : "U", "q" : "Q", 
    }
    
    new_list = []
    for letters in letters_lst:
        new_inner_list = []
        for let in letters:
            new_inner_list.append(let)
            if any([let in x for x in [ "a", "i", "u", "q", ]]):
                new_inner_list.append(xIrGa_dict[let])
        new_list.append(new_inner_list)
    
    return new_list
    

def get_letters(prawyAhAra):
    """ Returns all letters governed under the given prawyAhAra
    """
    
    start = prawyAhAra[0]
    end = prawyAhAra[1] + "!" if len(prawyAhAra) == 2 else prawyAhAra[2] + "!"
    
    all_forms = []
    cur_form = []
    started = False
    for let in mAheSvara_list:
        if started:
            if let == end:
                all_forms.append(cur_form[:])
            elif not "!" in let:
                cur_form.append(let)
            else:
                pass
        elif let == start:
            cur_form.append(let)
            started = True
        else:
            pass
    
    if prawyAhAra == "hal":
        all_forms.append([ "ha" ])
    
    # If xIrGa needs to be added, then use the following, else comment
    all_forms = add_xIrGa(all_forms)
    
    return all_forms
    

def print_prawyAhAra(prawyAhAra):
    """ """
    
    print(prawyAhAra + " -> " + str(get_letters(prawyAhAra)))

