s = input()
s = s.lower()
k = int(input())
l = len(s)
if k > l:
    print("impossible")
else:
    m= len(set(s))
    if k <= m:
        print(0)
    else:
        print(k-m)