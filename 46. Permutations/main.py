import itertools
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = list(itertools.permutations(nums)) 
        return res
