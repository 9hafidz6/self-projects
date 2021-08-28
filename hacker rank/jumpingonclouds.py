#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    # check if can jump by 2, if cannot jump by 1 
    jump = 0
    num = 0
    for i in range(len(c)):
        if num >= len(c) - 1:
            break
        
        if num+2 <= len(c) - 1:
            if c[num+2] == 0: # means can jump 2 spaces
                jump += 1
                num = num + 2
                continue
            
        if num+1 <= len(c) - 1:
            if c[num+1] == 0:
                jump += 1
                num = num + 1
                continue
            
        print(num)
                
    # print(jump)
    return jump

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
