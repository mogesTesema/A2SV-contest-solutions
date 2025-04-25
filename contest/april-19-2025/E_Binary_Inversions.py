

def solve():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
    
        a = list(map(int, input().split()))
       
        
        
        count_1 = 0
        original_inversions = 0
        for num in a:
            if num == 1:
                count_1 += 1
            else:
                original_inversions += count_1
        
        
        max_gain = 0
        count_1_left = 0
        count_0_right = a.count(0)
        
        for i in range(n):
            if a[i] == 1:
                
                gain = count_1_left - (count_0_right)
                max_gain = max(max_gain, gain)
                count_1_left += 1
            else:
               
                gain = (count_0_right - 1) - count_1_left
                max_gain = max(max_gain, gain)
                count_0_right -= 1
        
        print(original_inversions + max_gain)

solve()