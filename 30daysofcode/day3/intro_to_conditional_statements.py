#!/bin/python3

import math
import os
import random
import re
import sys

def solution(n):
    if n % 2:
        print('Weird')
    elif 2<= n <= 5:
        print('Not Weird')
    elif 6<= n <= 20:
        print('Weird')
    elif n > 20:
        print('Not Weird')


if __name__ == '__main__':
    N = int(input())
    solution(N)
