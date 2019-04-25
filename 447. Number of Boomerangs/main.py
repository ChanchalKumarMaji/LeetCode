from collections import defaultdict 
class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def distance(t1, t2):
            return (t1[0]-t2[0])**2 + (t1[1]-t2[1])**2 
        
        res = 0
        for i in range(len(points)):
            d = defaultdict(int) 
            for j in range(len(points)):
                d[distance(points[i], points[j])] += 1
            for v in d.values():
                res += v*(v-1) 
                
        return res
