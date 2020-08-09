class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        res = list(range(1, 2001))
        for e in arr:
            res.remove(e)
        return res[k-1]
