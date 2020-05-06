class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        n = len(candies)
        res = [True] * n
        for i in range(n):
            if candies[i] + extraCandies < m:
                res[i] = False
        return res
