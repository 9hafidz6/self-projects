#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    # maybe do counting sort or dictionary
    elem = []
    res = 0
    for i in range(101):
        elem.append(0)
            
    for i in ar:
        elem[i] += 1

    print(elem)

    for i in elem:
        # print(i // 2)
        res += i // 2
    
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    # print(n)
    ar = list(map(int, input().rstrip().split()))
    # print(f"this is {ar}")
    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
