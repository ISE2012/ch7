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
    new_balances = []
    for i in range(len(balances)):
        new_balances.append(balances[i] * (1 + rate))
        
    return new_balances

def test():
    amounts = [1000, 2200, 800, 360]
    rate = 0.05
    new_balances = addInt(amounts, rate)
    print(amounts)
    print(new_balances)
   
test()



