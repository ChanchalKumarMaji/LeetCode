class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        s = sum(cardPoints[:k])
        res = s
        for i in range(1, k+1):
            s += cardPoints[-i] - cardPoints[k-i]
            res = max(res, s)
        return res
