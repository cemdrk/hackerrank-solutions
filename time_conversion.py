#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hour = s[:2]
    period = s[-2:]

    if (period == 'PM' and hour != '12') or (period == 'AM' and hour == '12'):
        hour = s[:2]
        hour = (int(hour) + 12) % 24
        s = str(hour).zfill(2) + s[2:]
        print(s)

    return s[:-2]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
