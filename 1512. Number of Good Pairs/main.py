class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    res += 1
        return res
