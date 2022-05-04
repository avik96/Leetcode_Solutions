class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        mind, mini = 25000, -1
        for i in range(len(points)) :
            xp, yp = points[i][0], points[i][1]
            if ((xp == x or yp == y)):
                if((abs(xp-x) + abs(yp-y)) < mind):
                    mind = (abs(xp-x) + abs(yp-y))
                    mini = i
                
        if(mini >= 0):
           return mini
        else:
            return -1
            
        