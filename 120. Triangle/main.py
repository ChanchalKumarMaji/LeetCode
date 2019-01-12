class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = triangle[-1] 
        n = len(triangle)
        
        for i in range(n-2, -1, -1):
            l = triangle[i] 
            for j in range(len(l)):
                dp[j] = l[j] + min(dp[j], dp[j+1]) 
                
        return dp[0]
