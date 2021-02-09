from collections import Counter
import itertools

dict_lst = []
query_lst = []
count_lst = []
len_dict_lst = int(input())
for i in range(0, len_dict_lst):
    a = input()
    dict_lst.append(a)

len_query_lst = int(input())
for j in range(0, len_query_lst):
    b = input()
    bn = ["".join(perm) for perm in itertools.permutations(b)]
    count=0
    for l in bn:
        if l in dict_lst:
            count+=1
    count_lst.append(count)
print(count_lst)


# print(query_lst)
# def all_perms(elements):
#     print("-1--elements---", elements)
#     if len(elements) <= 1:
#         print("iffffffff", elements)
#         return elements
#     else:
#         print("-2--elements---", elements)
#         print("===elements[1:]===", elements[1:])
#         tmp = []
#         for perm in all_perms(elements[1:]):
#             print("---perm---", perm)
#             for i in range(len(elements)):
#                 print("-3--elements---", elements)
#                 print('---i---', i)
#                 print('---perm[:i]---', perm[:i])
#                 print('---elements[0:1]---', elements[0:1])
#                 print('---perm[i:]---', perm[i:])
#                 tmp.append(perm[:i] + elements[0:1] + perm[i:])
#         print("---temp---", tmp)
#         return tmp

# count_lst = []
# for k in query_lst:
#     bn = ["".join(perm) for perm in itertools.permutations(k)]
#     print("========bn=========",bn)
#     # all_perms(k)
#     count = 0
#     for m in bn:
#         if m in dict_lst:
#             count += 1
#     count_lst.append(count)
# print('========countlst===========',count_lst)
