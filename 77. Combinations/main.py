import itertools
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = list(itertools.combinations([i+1 for i in range(n)], k)) 
        return res
