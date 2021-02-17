import math
import os
import random
import re
import sys


# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    temp_alpha = 97

    emp_dict = {}

    for i in range(26):
        emp_dict.update({
            chr(temp_alpha): h[i]
        })
        temp_alpha += 1

    lst = []
    for j in word:
        lst.append(emp_dict.get(j))

    print(max(lst) * len(word))
    return (max(lst) * len(word))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    # fptr.write(str(result) + '\n')

    # fptr.close()
