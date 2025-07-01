n,s = map(int,input().split())
nums = list(map (int,input().split()))
max_length = 0
current_sum = 0
left = 0
for i in range(len(nums)):
    current_sum += nums[i]
    if current_sum > s:
        current_sum -= nums[left]
        left += 1
    max_length = max(max_length,i-left + 1)
print(max_length)

    
