def sum():
    a,b,c =list(map(int, input().split()))
    if a+b==c or a+c==b or b+c==a:
        print("yes")
    else:
        print("no")
test= int(input())
for i in range(test):
    sum()