class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        d = collections.defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                d[i+j].append(nums[i][j])
        for k in sorted(d):
            res += d[k][::-1]
        return res
