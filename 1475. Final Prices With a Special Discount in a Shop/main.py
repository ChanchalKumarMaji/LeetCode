class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        res = [0] * n
        for i in range(n):
            m = 0
            for j in range(i+1, n):
                if prices[j] <= prices[i]:
                    m = prices[j]
                    break
            res[i] = prices[i] - m
        return res
