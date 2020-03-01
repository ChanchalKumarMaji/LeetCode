class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        for i in range(n):
            for j in range(n):
                if i != j and nums[j] < nums[i]:
                    res[i] += 1
        return res
