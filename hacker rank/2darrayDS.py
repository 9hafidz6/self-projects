#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
def checkHourglass(i,j,arr):
    hoursum = arr[i][j]
    steps = [
    [-1,0], #up
    [1,0], #down
    [-1,1], #topright
    [-1,-1], #topleft
    [1,-1], #downleft
    [1,1] #downright
    ]
    
    for [ix,jx] in steps:
        # print(f"{ix} {jx}")
        hoursum += arr[i+ix][j+jx]
    # print(hoursum)
    return hoursum

def checkboundary(i,j,rowlen,collen):
    if i == 0 or i == rowlen or j == 0 or j == collen:
        return False
    return True
    
def hourglassSum(arr):
    # Write your code here
    # iterate through all the elements in the array which are within bounds 
    Sum = -54
    
    for i,row in enumerate(arr):
        for j,col in enumerate(row):
            # print(arr[i][j])
            #check if not boundary
            if checkboundary(i,j,len(arr)-1,len(row)-1):
                tempsum = checkHourglass(i,j,arr)
                Sum = max(Sum,tempsum)
            else:
                continue
    return Sum
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
