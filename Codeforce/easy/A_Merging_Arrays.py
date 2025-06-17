n, m = map(int, input().split())
firstArray = list(map(int, input().split()))
secondArray = list(map(int,input().split()))
firstPointer = 0
secondPointer = 0
ans = []
while firstPointer < len(firstArray) and secondPointer < len(secondArray):
    if firstArray[firstPointer] < secondArray[secondPointer]:
        ans.append(firstArray[firstPointer])
        firstPointer += 1
    else:
        ans.append(secondArray[secondPointer])
        secondPointer += 1
ans.extend(firstArray[firstPointer:])
ans.extend(secondArray[secondPointer:])
for i in ans:
    print(i, end=" ")