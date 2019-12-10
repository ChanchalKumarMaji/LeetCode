import math

class Solution:
    def value(self, nums, k):
        res = 0
        for num in nums:
            res += math.ceil(num / k)
        return int(res)
    
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, h = 1, max(nums)
        while l < h:
            m = (l + h) // 2
            t = self.value(nums, m)
            if t > threshold:
                l = m + 1
            elif t <= threshold:
                h = m
            
        return h
