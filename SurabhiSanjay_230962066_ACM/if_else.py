#!/bin/python3

import math
import os
import random
import re
import sys


range1= range(2,6)
range2 = range(6,21)

if __name__ == '__main__':
    n = int(input().strip())
def is_even(n): 
    if n % 2 == 0 : 
       return True
    else: 
        return False

if not is_even(n) : 
    print("Weird") 
elif  n in (2,6):
    print("Not Weird")
elif is_even(n) and n in(6,20) : 
    print("Weird")
elif n % 2 == 0 and  n > 20: 
    print("Not Weird")
    
    


