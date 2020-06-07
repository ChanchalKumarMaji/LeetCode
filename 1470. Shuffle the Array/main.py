class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = [0 for _ in range(2*n)]
        for i, val in enumerate(nums[:n]):
            res[2*i] = val
        for i, val in enumerate(nums[n:]):
            res[2*i+1] = val
        return res
