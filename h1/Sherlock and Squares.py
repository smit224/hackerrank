import math

t_case = int(input())

for i in range(0, t_case):
    count = 0
    s_num = int(input())
    e_num = int(input())
    for j in range(s_num, e_num + 1):
        root = int(math.sqrt(j))
        if int(root + 0.5) ** 2 == j:
            count += 1

    print(count)

# for i in range(t_case):
#     root = int(math.sqrt(i))
#     print("=======", root)
# a = int(math.sqrt(25))
# print(a)
