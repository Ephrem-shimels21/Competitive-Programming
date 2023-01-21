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
    upMovment = 0
    downMovment = 0
    numberValleys= 0
    for movement in path:
        previous = movement
        if movement == "D":
            if upMovment != 0:
                upMovment -=1
            elif upMovment == 0:
                downMovment+=1
        elif movement == "U":
            if downMovment != 0:
                downMovment -=1
            elif downMovment == 0:
                upMovment +=1
        if (upMovment == 0) and (downMovment == 0) and (previous == "U"):
            numberValleys += 1
    return numberValleys
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
