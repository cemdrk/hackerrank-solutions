#!/bin/python3

import os
import sys
from math import gcd
from functools import reduce



def gcd_list(numbers):
    return reduce(gcd, numbers)


def lcm_list(nums):
    largest = nums[0]
    for i in nums[1:]:
        largest = largest*i//gcd(largest, i)

    return largest


def getTotalX(a, b):
    total = 0

    largest_multiple = lcm_list(a)

    common_factor = gcd_list(b)

    if common_factor % largest_multiple == 0:
        total += 1

    for i in range(1, common_factor//2+1):
        if (common_factor % i == 0) and (i % largest_multiple == 0):
            total += 1

    return total



if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
