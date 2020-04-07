# 3011 거품정렬

n = int(input())
numListInput = input().strip()
numList = list(map(int, numListInput.split(' ')))

step = 0


for i in range(len(numList) - 1):
    nonChange = True
    for j in range(len(numList) - 1 - i):
        if numList[j] > numList[j+1]:
            numList[j], numList[j+1] = numList[j+1], numList[j]
            nonChange = False
    if nonChange:
        break
    step += 1

print(step)