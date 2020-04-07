n = int(input())
inputLine = input().strip()
nums = inputLine.split(' ')

sortedNums = sorted(nums, key=lambda x: int(x))

dictNums = {}
count = 0

for sNum in sortedNums:
    dictNums[str(sNum)] = count
    count += 1

seqArr = []

for num in nums:
    seqArr.append(str(dictNums[num]))

print(' '.join(seqArr))