#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    index = n - 1
    while index > 0:
        if arr[index] < arr[index-1]:
            temp=arr[index]
            arr[index] = arr[index -1]
            print(" ".join(map(str,arr)))
            arr[index-1]=temp
        index = index -1
    print(" ".join(map(str,arr)))
            
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
