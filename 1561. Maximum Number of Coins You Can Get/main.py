class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        k = len(piles) // 3
        res = 0
        c = 0
        #print(piles[:-k])
        for i, val in enumerate(piles[:-k]):
            if c > k:
                break
            if i % 2 == 1:
                res += val
                c += 1
        return res
