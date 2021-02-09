s = (input())
k = int(input())

lst = []
if (len(s))%k == 0:
    count = int(len(s)/k)
    print("============Count===========",count)
    a = count
    for i in range(0,count):
        b = s[i:a]
        lst.append(b)
        a += count
    print(lst)

    for j in lst:
        c = ''.join(sorted(set(j), key=j.index))
        print(c)
# df = input()
# count = 0
# for j in df:
#     count += 1
# print(count)

s = input()
k = int(input())
num_subsegments = int(len(s) / k)
print("=============len(s)==========",len(s))
print("------------num_segments---------",num_subsegments)

for index in range(num_subsegments):
    # Subsegment string
    print("----------index------------",index)
    print("----------index * k------------", index * k)
    print("----------(index + 1) * k------------", (index + 1) * k)
    t = s[index * k: (index + 1) * k]
    print("------t-----",t)

    # Subsequence string having distinct characters
    u = ""

    # If a character is not already in 'u', append
    for c in t:
        if c not in u:
            u += c

    # Print final converted string
    print(u)