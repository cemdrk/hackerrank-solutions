#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    result = 0
    
    for i in range(len(s)):
        square_sum = sum(s[i:i+m])
        if square_sum == d:
            result += 1

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
