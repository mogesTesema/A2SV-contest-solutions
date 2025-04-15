def solve():
    n, k = map(int, input().split())
    letter = input()
    if "W" not in letter:
        print(0)
        return
    if "B" * k in letter:
        print(0)
        return
    minimumW = float('inf')
    windowWCount = letter[:k].count("W")
    minimumW = min(minimumW, windowWCount)
    for i in range(k, n):
        if letter[i - k] == 'W':
            windowWCount -= 1
        if letter[i] == 'W':
            windowWCount += 1
        minimumW = min(minimumW, windowWCount)
    print(minimumW)
t = int(input())
for _ in range(t):
    solve()