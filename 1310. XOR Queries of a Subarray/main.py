class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        n = len(arr)
        dp = [0]*(n+1)
        for i in range(n):
            dp[i+1] = dp[i] ^ arr[i]
        for q in queries:
            res.append(dp[q[1]+1] ^ dp[q[0]])
        return res
