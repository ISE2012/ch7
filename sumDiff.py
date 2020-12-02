# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 11:31:03 2020

@author: ucobiz
"""

def sumDiff(x, y):
    sum = x + y
    diff = x - y
    return sum, diff

def main():
    num1 = int(input("Enter first number:  "))
    num2 = int(input("Enter second number: "))
    s, d = sumDiff(num1, num2)
    print("The sum is", s,"and the difference is", d)

main()
