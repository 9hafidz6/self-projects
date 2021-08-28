#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    res = 0
    start = False
    level = 0
    # treat sea level as 0, once it goes below 0, can start counting
    for i in path:
        print(i)
        if i == 'U':
            level += 1
            if start == True and level == 0:
                res += 1
        if i == 'D':
            level -= 1
            if level < 0:
                start = True
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
