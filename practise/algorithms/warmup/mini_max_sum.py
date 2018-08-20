#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min_val = min(arr)
    max_val = max(arr)
    sum_arr = sum(arr)

    print(sum_arr-max_val, sum_arr-min_val)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
