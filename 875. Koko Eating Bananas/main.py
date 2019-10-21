import math 

class Solution:
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        def check(k):
            return sum([math.ceil(p/k) for p in piles])<=H
        l, h = 1, max(piles)
        while l<h:
            mid = (l+h)//2
            if check(mid):
                h = mid
            else:
                l = mid+1
        return l
