#!/bin/python3
import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

def solution(arr, n):
    swap = 0
    for i in range(n):
        is_sorted = True
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap += 1
                is_sorted = False

        if is_sorted:
            break

    return swap

s = solution(a, n)

print('Array is sorted in %d swaps.' % (s))
print('First Element: %d\nLast Element: %d' %(a[0], a[-1]))
