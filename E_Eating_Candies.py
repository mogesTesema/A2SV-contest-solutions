"""
HOw to solve the problem?
1. understand the problem
    a. express in your term
    b. identify input and output
2. explore with concrete example
    a. basic test
    b. edge test
    c. invalid input test
3. break it down
  solution
  until left and right connect
    alice eat and compare with bob total, let smaller total go forward
    check if they are equal, asign counter left+1 + n-right
    
4. solve and simplify
5. refactore
2 1 4 2 4 1
"""
def solution():
    n = int(input())
    candies = list(map(int, input().split()))
    eated = 0
    totalEated =0
    left = 0
    right = n - 1
    aliceTotal = candies[left]
    left += 1
    eated += 1
    bobTotal = 0
    while(left <= right):
        if aliceTotal > bobTotal:
            bobTotal += candies[right]
            right -= 1
            eated += 1
            totalEated 
        elif aliceTotal < bobTotal:
            aliceTotal += candies[left]
            left += 1
            eated += 1
        if aliceTotal == bobTotal:
            totalEated = eated
            aliceTotal += candies[left]
            eated += 1
            left += 1
    print(totalEated)
t = int(input())
for _ in range(t):
    solution()

