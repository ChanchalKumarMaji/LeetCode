import math

class Solution:
    def getPointsInside(self, i, r, n, points):
        angles = []
        for j in range(n):
            if i != j and self.dis[i][j] <= 2*r:
                B = math.acos(self.dis[i][j] / (2*r))
                x1, y1 = points[i]
                x2, y2 = points[j]
                A = math.atan2((y1-y2), (x1-x2))
                a = A-B
                b = A+B
                angles.append((a, 0))
                angles.append((b, 1))
        angles.sort()
        count = 1
        res = 1
        for angle in angles:
            if angle[1] == 0:
                count += 1
            else:
                count -= 1
            if count > res:
                res = count
        return res
    
    def numPoints(self, points: List[List[int]], r: int) -> int:
        n = len(points)
        self.dis = [[0 for i in range(n)] for j in range(n)]
        for i in range(n-1):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                self.dis[i][j] = self.dis[j][i] = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        ans = 0
        for i in range(n):
            ans = max(ans, self.getPointsInside(i, r, n, points))
        return ans
