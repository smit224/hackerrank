#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the kangaroo function bel
def kangaroo(x1, v1, x2, v2):
    try:
        temp = (x2 - x1) / (v1 - v2)
        if (temp == math.floor(temp) and temp >= 0):
            print("YES")
            return "YES"
        else:
            print("NO")
            return "NO"
    except:
        print("NO")
        return "NO"


if __name__ == '__main__':
    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)
