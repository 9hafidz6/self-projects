#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#
res = 0

def swap(i,j,a):
    global res
    tempi = a[i]
    tempj = a[j]
    a[j] = tempi
    a[i] = tempj
    res += 1
    return a

def countSwaps(a):
    # Write your code here
    # iterate through the array from first index 
    # bubble sort is O(n^2) time complexity
    arrlen = len(a) 
    for i,elem1 in enumerate(a):
        for j,elem2 in enumerate(a[:len(a)-1]): 
            if a[j] > a[j+1] and j+1 <= len(a)-1:
                #swap
                a = swap(j,j+1,a)
            
    print(f"Array is sorted in {res} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
