# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 11:37:28 2020

@author: ucobiz
"""

def main():
    amount = 1000
    rate = 0.05
    addInt(amount, rate)
    print(amount)

def addInt(balance, rate):
    newBalance = balance * (1 + rate)
    balance = newBalance

main()
