import math
import os
import random
import re
import sys

#
#
# #
# # Complete the 'gradingStudents' function below.
# #
# # The function is expected to return an INTEGER_ARRAY.
# # The function accepts INTEGER_ARRAY grades as parameter.
# #
#
# def gradingStudents(grades):
#     # Write your code here
    # emp_lst = []
    # for i in grades:
    #     if i < 38:
    #         emp_lst.append(i)
    #     else:
    #         c = math.ceil(i / 5) * 5
    #         diff = c - i
    #         if diff < 3:
    #             i = c
    #             emp_lst.append(i)
    #         else:
    #             emp_lst.append(i)
    # print(emp_lst)
    # return emp_lst
#
#
# # creating an empty list
# lst = []
#
# # number of elemetns as input
# n = int(input())
#
# # iterating till the range
# for i in range(0, n):
#     ele = int(input())
#
#     lst.append(ele)  # adding the element
# print(lst)
# gradingStudents(lst)


# lst = []
# for i in range(0, 2):
#     ele = int(input())
#     lst.append(ele)
#     lst.sort()

s, t = map(int, input().split())
print(s, t)

a, b = map(int, input().split())
print(a, b)

m, n = map(int, input().split())
print(m, n)

apple_lst = []
for i in range(0, m):
    apple_val = int(input())
    print("_________apple_____", apple_val)
    apple_lst.append(apple_val)

print('______i______', apple_lst)

orange_lst = []
for j in range(0, n):
    orange_val = int(input())
    print("_________orange______", orange_val)
    orange_lst.append(orange_val)

print("________-j________", orange_lst)

final_apple_lst = []
for apple_add in apple_lst:
    add_apple = apple_add + a
    final_apple_lst.append(add_apple)
print(final_apple_lst)

final_orange_lst = []
for orange_add in orange_lst:
    add_orange = orange_add + b
    final_orange_lst.append(add_orange)
print(final_orange_lst)

count_apple = 0
for range_apple in final_apple_lst:
    print("_____________________________",range_apple)
    if (range_apple >= s and range_apple <= t):
        count_apple += 1

print("apple count", count_apple)

count_orange = 0
for range_orange in final_orange_lst:
    if (range_orange >= s and range_orange <= t):
        count_orange += 1
print("count orange", count_orange)
