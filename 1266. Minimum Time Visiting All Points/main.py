class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(1, len(points)):
            dx = abs(points[i][0] - points[i-1][0])
            dy = abs(points[i][1] - points[i-1][1])
            res += dx + dy - min(dx, dy)
        
        return res
