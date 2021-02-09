s = input().strip()
t = input().strip()
k = int(input().strip())

ls = len(s)
print('=======ls=========', ls)
lt = len(t)
print('=======lt=========', lt)

lcp = 0  # Length of common prefix
while lcp <= ls - 1 and lcp <= lt - 1 and s[lcp] == t[lcp]:
    print('==1======lcp===========', lcp)
    lcp += 1
print('==2======lcp===========', lcp)
print('==2======ls+lt===========', ls + lt)
print('==2======kkkk==========', k)
print('=========k >= ls + lt - 2 * lcp========', ls + lt - 2 * lcp)
print("======(k - ls - lt + 2 * lcp)=====", (k - ls - lt + 2 * lcp))
print("=========(k - ls - lt + 2 * lcp) % 2==========", (k - ls - lt + 2 * lcp) % 2)
if k >= ls + lt:
    print("Yes")

elif k >= ls + lt - 2 * lcp and (k - ls - lt + 2 * lcp) % 2 == 0:
    print("Yes")
else:
    print("No")
#
# def drdrdr(s, t, k):
#     print("=============")
#     ls = len(s)
#     lt = len(t)
#
#     scount = 0
#     sdc = 0
#     tdc = 0
#
#     i = 0
#     while (s[i] == t[i]):
#         print("=======s[i]========",s[i])
#         print("=======s[j]========", s[i])
#         i += 1
#         scount += 1
#
#     sdc = ls - scount
#     tdc = lt - scount
#
#     if k >= sdc + tdc:
#         return "Yes"
#     else:
#         return "No"
#
#
# if __name__ == '__main__':
#     s = input().strip()
#     t = input().strip()
#     k = int(input().strip())
#     result = drdrdr(s, t, k)
# help(str)
