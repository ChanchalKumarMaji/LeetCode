class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -float('inf')
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                t = (nums[i]-1) * (nums[j]-1)
                res = max(res, t)
        return res
