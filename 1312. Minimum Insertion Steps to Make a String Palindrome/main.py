class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for g in range(1, n):
            l, h = 0, g
            while h < n:
                if s[l] == s[h]:
                    dp[l][h] = dp[l+1][h-1]
                else:
                    dp[l][h] = min(dp[l][h-1], dp[l+1][h]) + 1
                l += 1
                h += 1
        return dp[0][n-1]
