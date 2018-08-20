#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    arr_len = len(arr)
    left_diag = 0
    right_diag = 0

    for i in range(arr_len):
        left_diag += arr[i][i]
        right_diag += arr[arr_len-i-1][i]

    return abs(left_diag - right_diag)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
