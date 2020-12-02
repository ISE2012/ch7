# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 05:43:42 2020

@author: ucobiz
"""

def happy():
    print("Happy Bday to you!")
    
def singFred():
    happy()
    happy()
    print("Happy Bday, Fred")
    happy()

def singLucy():
    happy()
    happy()
    print("Happy Bday, Lucy")
    happy()

def main():
    singFred() # sing Happy Birthday to Fred
    print()    # empty line between the two
    singLucy() # sing Happy Birthday to Lucy

main()



