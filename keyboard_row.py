class Solution:
    def findWords(self, words):
        row1 = {'e', 'q', 'u', 'o', 'y', 't', 'p', 'r', 'w', 'i'}
        row2 = {'s', 'a', 'h', 'f', 'g', 'd', 'k', 'l', 'j'}
        row3 = {'x', 'c', 'v', 'm', 'n', 'z', 'b'}
        on_row = []
        for i in words:
            k = i.lower()
            j = set(k)
            if j.issubset(row1) or j.issubset(row2) or j.issubset(row3):
                on_row.append(i)
        return on_row      
            
            

            
test = Solution()
print(test.findWords(["Hello","Alaska","Dad","Peace"]))       

