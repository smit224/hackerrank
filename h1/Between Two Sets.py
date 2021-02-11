#!/bin/python3
#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def find_lcm(num1, num2):
    if (num1 > num2):
        num = num1
        den = num2
    else:
        num = num2
        den = num1
    rem = num % den
    while (rem != 0):
        num = den
        den = rem
        rem = num % den
    gcd = den
    lcm = int(int(num1 * num2) / int(gcd))
    return lcm


def getTotalX(a, b):
    if len(a) > 1:
        num1 = a[0]
        num2 = a[1]
        lcm = find_lcm(num1, num2)
        for i in range(2, len(a)):
            lcm = find_lcm(lcm, a[i])
    else:
        lcm = a[0]
    intermediate_lst = []
    count = 0
    temp_var = 1
    temp = lcm
    while (temp < b[-1]):
        temp = lcm * temp_var
        intermediate_lst.append(temp)
        temp_var += 1
    b.sort()
    for i in intermediate_lst:
        flag = 0
        for j in b:
            if j % i != 0:
                flag = 1
                break
            else:
                pass
        if flag == 0:
            count += 1
    print(count)
    return count
    # Write your code here


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    # fptr.write(str(total) + '\n')
    #
    # fptr.close()
