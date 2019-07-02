class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k<1:
            return 0
        ans = left = 0 
        p = 1
        for right, val in enumerate(nums):
            p = p*val 
            while p >= k and left<=right: 
                p = p//nums[left]
                left += 1
            ans += right - left + 1
            
        return ans
