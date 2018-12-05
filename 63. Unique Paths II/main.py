class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])
        
        dp = [[0 for j in range(c)] for i in range(r)] 
        for i in range(r):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break
        for j in range(c):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break
        
        for i in range(1, r):
            for j in range(1, c):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                    
        return dp[-1][-1]
