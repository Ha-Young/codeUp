# 정렬을 빠르게

n = int(input())
numList = map(int, input().strip().split(' '))

countList = [0] * 100001

for num in numList:
    countList[num] += 1

for idx in range(len(countList)):
    while countList[idx] > 0:
        print(str(idx), end=" ")
        countList[idx] -= 1