class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        def remove(x):
            return list(dict.fromkeys(x))
        
        for i in range(0,len(arr)):
            for j in range(0,len(pieces)):
                for k in pieces[j]:
                    if arr[i] == k:
                        compare.append(pieces[j])

            compare = remove(compare)
                if arr[0:len(compare)] != compare:
                    break
                    return False  
        return True





compare = []
arr = [91,4,64,78]
pieces = [[78],[4,64],[91]]





