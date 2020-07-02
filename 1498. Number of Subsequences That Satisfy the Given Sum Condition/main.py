class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums)-1
        res = 0
        while l <= r:
            if nums[l] + nums[r] <= target:
                res += 1 << (r-l)
                l += 1
            else:
                r -= 1
            res = res % (1000_000_007)
        return res
