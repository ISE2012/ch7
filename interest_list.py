# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 11:46:26 2020

@author: ucobiz
"""

# interest_list.py
# Illustrates modification of a mutable parameter (a list)

# interest_list.py
# Illustrates modification of a mutable parameter (a list)

def addInt(balances, rate):
    for i in range(len(balances)):
        balances[i] = balances[i] * (1 + rate)

def test():
    amounts = [1000, 2200, 800, 360]
    rate = 0.05
    addInt(amounts, rate)
    print(amounts)
   
test()



