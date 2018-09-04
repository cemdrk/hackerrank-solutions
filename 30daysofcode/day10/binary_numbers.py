#!/bin/python3

import math
import os
import random
import re
import sys

def solution(n):
    result = 0

    num_bin = bin(n)[2:] + '0'
    length = len(num_bin)

    count = 0
    for i in range(length):
        if num_bin[i] == '0':
            if count > result:
                result = count

            count = 0
        else:
            count += 1

    return result




if __name__ == '__main__':
    n = int(input())
    print(solution(n))
