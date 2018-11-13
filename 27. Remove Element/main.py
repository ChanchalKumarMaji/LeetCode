class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l=len(nums)
        c=nums.count(val)
        for i in range(c):
            nums.remove(val)
        return l-c
