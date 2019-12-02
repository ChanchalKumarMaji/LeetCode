class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        x, y = toBeRemoved
        
        for interval in intervals:
            l, h = interval
            if l <= x <= h <= y:
                res.append([l, x])
            elif x <= l <= y <= h:
                res.append([y, h])
            elif l <= x <= y <= h:
                res.append([l, x])
                res.append([y, h])
            elif x <= l <= h <= y:
                continue
            else:
                res.append([l, h])
                
        return res
