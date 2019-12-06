class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        r, c = len(matrix), len(matrix[0])
        
        dp=[[0 for j in range(c)] for i in range(r)]
        
        for i in range(r):
            dp[i][0] = matrix[i][0]
            
        for j in range(c):    
            dp[0][j] = matrix[0][j]
        
        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j]) +1
        
        print(dp)
        
        res = 0
        for i in range(r):
            for j in range(c):
                res += dp[i][j]
        
        return res
