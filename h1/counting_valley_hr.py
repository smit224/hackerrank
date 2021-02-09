import sys


def countingValleys(n, steps):
    seaLevel = valley = 0

    for step in steps:
        if step == 'U':
            seaLevel += 1
        else:
            seaLevel -= 1
        print(seaLevel)
        if step == 'U' and seaLevel == 0:
            valley += 1
            print('============if============valley==========',valley)
    print("________VALLEYY__________",valley)
    return valley

n=int(input())
steps = list( str(i) for i in input())[:n]
# steps = []
# for i in range(n):
#     a = input()
#     steps.append(a)
countingValleys(n,steps)