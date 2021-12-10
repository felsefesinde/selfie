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

from selfie import *

#-----------------------SAMPLE CODE FOR RUNNING selfie(args, priv)-------------------------------------   
args = input("Please enter the arguements of your __init__ function [seperated by commas]: def __init__(")
#THERE SHOULD NOT BE A PARANTHESIS AT THE END OF THE INPUT. ONLY THE ATTRIBUTES SHOULD BE ENTERED LIKE: name, surname, city, country
priv_pub = input("Would you like to make your arguements private attributes? [y:Yes | n: No]")
print(selfie(args, priv_pub))

#-----------------------SAMPLE CODE FOR RUNNING getinit(get)------------------------------------- 
get = input("Pleae enter the arguements that you want to get [seperated by commas]: ")
#THERE SHOULD NOT BE A PARANTHESIS AT THE END OF THE INPUT. ONLY THE ATTRIBUTES SHOULD BE ENTERED LIKE: name, surname, city, country
print(getinit(get))

#-----------------------SAMPLE CODE FOR RUNNING setinit(setf)------------------------------------- 
setf = input("Pleae enter the arguements that you want to set [seperated by commas]: ")
#THERE SHOULD NOT BE A PARANTHESIS AT THE END OF THE INPUT. ONLY THE ATTRIBUTES SHOULD BE ENTERED LIKE: name, surname, city, country
print(setinit(setf))

input("Press Enter to Exit the App...")
