class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def check(t, a, dp):
            n=len(t)
            for k in range(1, n):
                if dp[a+0][a+k-1] and dp[a+k][a+n-1]:
                    return 1
            return 0   
        
        n=len(s)
        dp=[[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n-i):
                t=s[j:j+i+1]
                if t in wordDict:
                    dp[j][j+i]=1
                else:
                    dp[j][j+i]=check(t, j, dp)
                    
        return dp[0][n-1]==1
