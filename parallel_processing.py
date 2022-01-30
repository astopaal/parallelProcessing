#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minTime' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY files
#  2. INTEGER numCores
#  3. INTEGER limit
#

def minTime(files, numCores, limit):
    # Write your code here
    n = len(files)
    
    time = 0
    limitcounter = 0
    
    candivide = []
    cantdivide = []
    
    for i in files:
        if i % numCores == 0:
            candivide.append(i)
        else:
            cantdivide.append(i)
    
    candivide.sort(reverse = True)
    
    for i in cantdivide:
        time += i
    for i in candivide:
        if limitcounter < limit:
            time += (i/numCores)
            limitcounter += 1
        else:
            time += i
            
    return int(time)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    files_count = int(input().strip())

    files = []

    for _ in range(files_count):
        files_item = int(input().strip())
        files.append(files_item)

    numCores = int(input().strip())

    limit = int(input().strip())

    result = minTime(files, numCores, limit)

    fptr.write(str(result) + '\n')

    fptr.close()
