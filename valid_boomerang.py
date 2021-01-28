class Solution:
    def isBoomerang(self, points):
       
        grad1 = (points[1][1]-points[0][1])/(points[1][0]-points[0][0])
        grad2 = (points[2][1]-points[0][1])/(points[2][0]-points[0][0])
        return grad2
        

points = [[0,0],[0,2],[2,1]]
test = Solution()
print(test.isBoomerang(points))
