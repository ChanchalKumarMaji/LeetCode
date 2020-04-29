class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        res = 0
        
        for i in range(len(satisfaction)):
            res = max(res, sum([(i+1)*e for i, e in enumerate(satisfaction[i:])]))
        return res
