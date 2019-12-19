class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        right = -1
        for i in range(len(intervals)):
            if right < intervals[i][1]:
                right = intervals[i][1]
                res += 1
        
        return res
