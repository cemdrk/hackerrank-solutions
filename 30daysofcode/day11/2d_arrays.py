#!/bin/python3

import math
import os
import random
import re
import sys


def solution(arr):
    total = float('-inf')

    for i in range(6-2):
        for j in range(6-2):
                subtotal = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]

                if subtotal > total:
                    total = subtotal

    return total


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(solution(arr))
