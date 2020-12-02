# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 06:33:05 2020

@author: ucobiz
"""

def happy():
    print("Happy Bday to you!")

def sing(person, age):
    happy()
    happy()
    print("Happy Bday,", person)
    print("You're already", age, "years old")
    happy()

def main():
    sing(30, "Fred")

main()
