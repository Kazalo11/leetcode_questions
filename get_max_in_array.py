class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        for i in range(2,n+1):
            if n % 2 == 0:
                i = int(n/2)
                x = (self.getMaximumGenerated(i))
                
            else:
                i = int((n-1)/2)
                x= self.getMaximumGenerated(i) + self.getMaximumGenerated(i+1)
                


            
test = Solution()
print(test.getMaximumGenerated(7))