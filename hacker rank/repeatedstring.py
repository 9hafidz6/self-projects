#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    # find how many times 'a' is found 

    num = 0
    numA = s.count("a")
    length = n // len(s)
    remainder = n % len(s)
    num = numA * length
    
    for i in range(remainder):
        if s[i] == "a":
            num += 1
    
#=========================================

    # num = 0
    # length = 0
    # for i in range(n):
    #     length += len(s)
    #     if length >= n:
    #         break
    #     num += s.count("a")
    #     print(num)
    
    # remainder = length - n
    
    # for j in range(remainder):
    #     if s[j] == "a":
    #         num += 1
    #=========================================
    # fullString = s * n
    # slicedstring = fullString[:n+1]
    # num = slicedstring.count("a")
    return num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
