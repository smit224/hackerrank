def sockMerchant(n, ar):
    my_dict = {i:ar.count(i) for i in ar}
    # my_dict = {}
    # for i in ar:
    #     my_dict.update({
    #         i:ar.count(i)
    #     })
    # print("------------",my_dict)
    count = 0
    for j in my_dict.values():
        nn = int(j/2)
        count += nn
    print(count)
    return count

n = int(input())
ar = list(int(i) for i in input().split())[:n]
# ar = list(map(int, input().strip().split()))[:n]
print(ar)
sockMerchant(n,ar)