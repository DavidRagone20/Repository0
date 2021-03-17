# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 10:17:38 2021

This problem makes use of the random module, 
either a for loop or while loop and if...elif...else. 
Try entering import random into the shell, then explore the functions 
within the module. For this activity you will need to simulate rolling dice.
Can you figure out a way to “randomly roll” a single 6-sided die? 
Now write a program that simulates rolling two dice
and keeps track of the total of each roll, and how many times
in the simulation that total was "rolled".  
The program will then output each possible roll total and 
the number of times it occurred as a pipe or other symbol.  
Allow a user to specify how many rolls to simulate.

@author: dragone1
"""

import numpy as np
from collections import Counter

MIN = 2
MAX = 12

#number of times rolling a pair of dice will be simulated
num_rolls = int(input("How many times would you like to roll the dice? : "))
print("\nSimulating rolling a pair of dice", num_rolls, "time(s)\n")
print("-"*50)

#generates a list of numbers 2-12 randomly, the length of the list = num_rolls
roll_list = np.random.randint(MIN, MAX, num_rolls)

#counts up number of times a number<=12 occured
#only numbers <=12 would occur because of how the rolls_list is generated
c = Counter(roll_list).most_common(12)

value = 2
while value <= 12:  
    d = Counter(roll_list).get(value)  
    if value <10:
        if d != None:
            print(f"{value:.0f}s  :", d*"/")
        else :
            print(f"{value:.0f}s  :")
    else:
        if d != None:
            print(f"{value:.0f}s :", d*"/")
        else :
            print(f"{value:.0f}s :")
    value = value+1