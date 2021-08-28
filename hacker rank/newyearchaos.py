#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def swap(index1,index2,elem,res):
    # check if can swap ie, 2 positions max
    # use remove and insert 
    # index1 is the original 
    # index2 is the final 
    
    swapNum = index1 - index2
    temp = elem[index1]
    elem.remove(elem[index1])
    # print(elem)
    elem.insert(index2,temp)
    # print(elem)
    res += swapNum
    return elem,res

def minimumBribes(q):
    # Write your code here
    # assuming initial queue is ordered ie. 1 2 3 4 5 etc  
    res = 0
    elem = []
    for i in range(len(q)):
        elem.append(i+1) # fill the elem list with initial ordered numbers
        
    # can start comparing with ordered with final pattern
    for j in range(len(q)):
        if elem[j] != q[j]: # means there is a swap, can only swap to front
            # give the index of supposed and current index 
            index1 = elem.index(q[j])
            index2 = elem.index(elem[j])
            # print(f"interation {i}, index 1:{index1} index 2:{index2}")
            
            if (index1-index2) > 2:
                print("Too chaotic")
                return 0
            else:
                elem,res = swap(index1,index2,elem,res)
            # num1 = elem[i]
            # num2 = q[i]
            # elem = swap(num1,num2,elem)
        else:
            continue
    print(res)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
