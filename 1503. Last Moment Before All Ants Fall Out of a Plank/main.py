class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        res = 0
        for i, l in enumerate(left):
            res = max(res, l)
        for i, r in enumerate(right):
            res = max(res, n-r)
        return res
