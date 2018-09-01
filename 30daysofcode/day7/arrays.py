#!/bin/python3

import math
import os
import random
import re
import sys


def solution(ar):
    # print(' '.join(map(str, ar[::-1])))
    print(*ar[::-1])

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    solution(arr)
