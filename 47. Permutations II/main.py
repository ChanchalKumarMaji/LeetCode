import itertools
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = list(itertools.permutations(nums)) 
        return list(set(res))
