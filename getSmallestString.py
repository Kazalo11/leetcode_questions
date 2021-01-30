class Solution:
    def getSmallestString(self, n,k):
        smallest = []
        while k >= 1:
            addition = k-n+1
            if addition >= 26:
                smallest.append("z")
                k-=26
                n-=1
            elif addition < 26:
                smallest.append(chr(addition+96))
                k = k - addition
                n-=1
        smallest = ''.join(smallest)
        return smallest[::-1]

test = Solution()
print(test.getSmallestString(3,27))

            