#!/bin/python3

import math
import os
import random
import re
import sys


def solution(n):
    for i in range(1, 11):
        print('%d x %d = %d' % (n, i, n*i))

if __name__ == '__main__':
    n = int(input())
    solution(n)
