class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        n = len(A)
        dp = [[float("inf")]*n for _ in range(n)]
        for j in range(n):
            dp[n-1][j] = A[n-1][j]
        for i in range(n-2, -1, -1):
            for j in range(n):
                for dc in [-1, 0, 1]:
                    if j + dc >= 0 and j + dc < n:
                        dp[i][j] = min(dp[i][j], dp[i+1][j+dc]+A[i][j])
        
        return min(dp[0])
