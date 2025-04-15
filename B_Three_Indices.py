def solve():
    n = int(input())
    p = list(map(int, input().split()))

    for j in range(1, n - 1):
        for i in range(j):
            for k in range(j + 1, n):
                if p[i] < p[j] and p[j] > p[k]:
                    print("YES")
                    print(i + 1, j + 1, k + 1)
                    return
    print("NO")

t = int(input())
for _ in range(t):
    solve()