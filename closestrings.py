class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        word1 = ''.join(sorted(word1))
        word2 = ''.join(sorted(word2))
        if word1 == word2:
            return True
        freq1 = {}
        freq2 = {}
        for i in word1:
            if i in freq1:
                freq1[i]+=1
            else:
                freq1[i] = 1
        for j in word2:
            if j in freq2:
                freq2[j]+=1
            else:
                freq2[j] = 1
        freq1 = list(freq1.values())
        freq2 = list(freq2.values())
        freq1.sort()
        freq2.sort()
        return( freq1 == freq2)

     

test = Solution()
print(test.closeStrings("cabbba","abbccc"))
