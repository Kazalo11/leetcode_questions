class Solution:
    def uniqueOccurrences(self, arr):
        arr2 = list(set(arr))
        if arr == arr2:
            return False
        count = [0]*len(arr2)
        for i in range(0,len(arr2)):
            for j in range(0,len(arr)):
                if arr2[i] == arr[j]:
                    count[i]+=1
        return list(set(count)) 

test = Solution()
print(test.uniqueOccurrences([1,2,2,1,4,3]))