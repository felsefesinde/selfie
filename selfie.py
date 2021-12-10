# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 11:34:40 2021

@author: Burak Alanyalıoğlu
GitHub: @felsefesinde
Instagram: @felsefesinde
YouTube: Felsefesinde
Twitter: @felsefesinde & @binichburak
MIT License

Copyright (c) 2021 Burak Alanyalıoğlu
"""

def selfie(args, priv):
    method = f"def __init__(self, {args}):\n"
    args = args.split(", ")
    if priv.lower() == "y":
        for i in range (len(args)):
            method += f"\tself.__{args[i]} = {args[i]}\n"
        return method
    if priv.lower() == "n":
        for i in range (len(args)):
            method += f"self.{args[i]} = {args[i]}\n"
        return method

def getinit(get):
    get = get.split(", ")
    org_func = "def get_"
    list_of_get = []
    res = ""
    for i in range (len(get)):
        org_func += f"{get[i]}"
        org_func += "(self):\n"
        org_func += f"\treturn self.__{get[i]}\n"
        list_of_get.append(org_func)
        org_func = "def get"
    for elements in list_of_get:
        res += elements
    return res

def setinit(setf):
    setf = setf.split(", ")
    org_func = "def set_"
    list_of_set = []
    res = ""
    for i in range (len(setf)):
        org_func += f"{setf[i]}"
        org_func += "(self):\n"
        org_func += f"\treturn self.__{setf[i]}\n"
        list_of_set.append(org_func)
        org_func = "def set"
    for elements in list_of_set:
        res += elements
    return res
 



