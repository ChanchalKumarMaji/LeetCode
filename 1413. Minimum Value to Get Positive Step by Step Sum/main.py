class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        res = nums[0]
        s = 0
        for num in nums:
            s += num
            res = min(res, s)
        if res >= 1:
            return 1
        return -res + 1
