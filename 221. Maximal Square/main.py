class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        r=len(matrix)
        if r==0:
            return 0
        c=len(matrix[0])
        
        dp=[[0 for j in range(c)] for i in range(r)]
        
        for i in range(r):
            dp[i][0]=int(matrix[i][0])
            
        for j in range(c):    
            dp[0][j]=int(matrix[0][j])
        
        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][j]=="1":
                    dp[i][j]=min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j]) +1
                    
        m=0
        for i in range(r):
            for j in range(c):
                m=max(m,dp[i][j])
        
        return m*m
