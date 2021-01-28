import math
class Solution:
    def countPrimeSetBits(self, L,R):
        count = 0
        for i in range(L,R+1):
            bits = str(bin(i)[2:])
            ones = bits.count("1")
            if self.isPrime(ones) and ones != 1:
                count+=1
        return count


    def isPrime(self,n):
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        
        return True

            
test = Solution()
print(test.countPrimeSetBits(10,15))        