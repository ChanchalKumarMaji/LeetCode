class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        k=1
        m=0
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                k+=1
            else:
                m=max(m,k)
                k=1
        
        m=max(m,k)
        return m
