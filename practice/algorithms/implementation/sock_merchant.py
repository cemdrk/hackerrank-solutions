#!/bin/python3

import math
import os
import random
import re
import sys



def sockMerchant(n, ar):
    que = []
    pairs = 0

    for s in ar:
        if s not in que:
            que.append(s)
        else:
            pairs += 1
            que.remove(s)

    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
