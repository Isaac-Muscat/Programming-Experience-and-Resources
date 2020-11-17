#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 09:35:43 2020

@author: isaacmuscat
"""

print("Note: This program only converts to bases between 2 and 16")
number = input("Input the number to be converted: ")
base = input("Input the base of the number: ")
base_conv = input("Input the base you want the number to be converted to: ")
dec_num = 0
new_num = ''

index_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

if (base != 10):
    count = len(number)-1
    for c in number:
        dec_num += index_nums.index(c) * (int(base)**count)
        count -= 1
else:
    dec_num = number
    

result = dec_num
while True:
    remainder = int(result % int(base_conv))
    result = int(result/int(base_conv))
    new_num = index_nums[remainder] + new_num
    if(result <= 0):
        break

print("The converted number is: " + new_num)