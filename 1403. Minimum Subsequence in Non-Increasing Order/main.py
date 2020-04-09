class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        s = sum(nums)
        for i in range(len(nums)):
            if 2 * sum(nums[:i+1]) > s:
                return nums[:i+1]
