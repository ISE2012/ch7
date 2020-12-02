# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 05:53:17 2020

@author: ucobiz
"""

def happy():
    print("Happy Bday to you!")

def sing(person):
    happy()
    happy()
    print("Happy Bday,", person)
    happy()

def main():
    whose = input("Whose birthday? ")
    sing(whose)

main()