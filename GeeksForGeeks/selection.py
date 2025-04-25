class Solution: 
    def selectionSort(self, arr):
    #    return arr.sort()
        for i in range(len(arr)):
            smaller  = i
            for j in range(i+1,len(arr)):
                if arr[smaller] > arr[j]:
                    smaller = j
            temp = arr[i]
            arr[i] = arr[smaller]
            arr[smaller] = temp
        return arr
x = Solution()
x = x.selectionSort([14,252,6,63,2,25])
print(x)