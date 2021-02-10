#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    # print("====",len(arr))
    count_1 = 0
    count_2 = 0
    seq_1 = 0
    seq_2 = len(arr) - 1
    for i in arr:
        count_1 += i[seq_1]
        seq_1 += 1
        count_2 += i[seq_2]
        seq_2 -= 1
    final_sum = abs(count_1 - count_2)
    print(final_sum)
    return final_sum


if __name__ == '__main__':

    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
