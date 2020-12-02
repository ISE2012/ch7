# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 11:37:58 2020

@author: ucobiz
"""

def addInt(balance, rate):
    newBalance = balance * (1 + rate)
    return newBalance

def main():
    amount = 1000
    rate = 0.05
    amount = addInt(amount, rate)
    print(amount)

main()
