#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    n = len(arr)
    pos = 0
    neg = 0

    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1

    print(pos/n)
    print(neg/n)
    print((n-(pos+neg))/n)




if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
