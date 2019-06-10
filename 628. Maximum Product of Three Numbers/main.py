class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums=nums
        length=len(nums)
        nums.sort()
        m=max(nums[0]*nums[1]*nums[2] , nums[length-1]*nums[length-2]*nums[length-3] , nums[0]*nums[1]*nums[length-1] , nums[0]*nums[length-1]*nums[length-2])
        return m
