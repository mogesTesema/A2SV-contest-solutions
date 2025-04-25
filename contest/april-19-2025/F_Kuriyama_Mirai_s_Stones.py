n = int(input())
vs = list(map(int, input().split()))
vs2 = vs.copy()
t = int(input())
for i in range(1,n):
    vs[i] = vs[i-1] +vs[i]
vs2.sort()
for i in range(1,n):
    vs2[i] = vs2[i-1] +vs2[i]
for i in range(t):
    type, l, r = list(map(int, input().split()))
    l -= 1
    r -= 1
    if type == 1:
        if  l == 0:
            print(vs[r])
        else:
            print(vs[r]-vs[l-1])  
    else:
        if l == 0:
            print(vs2[r])
        else:
            print(vs2[r]-vs2[l-1])
    
