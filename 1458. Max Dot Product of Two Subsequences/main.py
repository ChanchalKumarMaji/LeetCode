class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0 for j in range(m+1)] for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] = max((dp[i-1][j-1]+nums1[j-1]*nums2[i-1]), dp[i][j-1], dp[i-1][j])
        if dp[n][m] == 0:
            return max([i*j for i in nums1 for j in nums2])
        return dp[n][m]
