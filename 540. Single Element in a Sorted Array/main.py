class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        for num in nums:
            c=c^num
        return c
