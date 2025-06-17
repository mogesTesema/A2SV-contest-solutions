n, m = map(int,input().split())
first = list(map(int, input().split()))
second = list(map(int, input().split()))
firstP = 0

ans = []
for secondP in range(m):
    while ( firstP < n and first[firstP]< second[secondP]):
        firstP += 1
    ans.append(firstP)
for i in ans:
    print(i, end=" ")




