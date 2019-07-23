class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        length=len(points)
        m=0
        for i1 in range(length):
            for i2 in range(length):
                if i1==i2:
                    continue
                for i3 in range(length):
                    if i2==i3:
                        continue
                    area=abs(points[i1][0]*points[i2][1]+points[i3][0]*points[i1][1]+points[i2][0]*points[i3][1]-points[i1][0]*points[i3][1]-points[i2][0]*points[i1][1]-points[i3][0]*points[i2][1])
                    
                    m=max(m,area)
                    
        return 0.5*m
