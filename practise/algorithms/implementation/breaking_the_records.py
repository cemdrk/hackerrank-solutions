#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    min_record = scores[0]
    max_record = scores[0]

    min_break = 0
    max_break = 0

    for s in scores[1:]:
        if s < min_record:
            min_record = s
            min_break += 1
        elif s > max_record:
            max_record = s
            max_break += 1

    return max_break, min_break


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
