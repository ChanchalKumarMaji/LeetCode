class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if s[0] == '0':
            return 0
        
        dp = [0 for i in range(len(s) + 1)]
        
        dp[0] = 1 
        dp[1] = 1
        
        for i in range(2, len(s)+1): 
            if (1 <= int(s[i-1]) <= 9) and ((1 <= int(s[i-2:i]) <= 26) and (1 <= int(s[i-2]) <= 2)):
                dp[i] = dp[i-1] + dp[i-2]
            elif (1 <= int(s[i-1]) <= 9):
                dp[i] = dp[i-1]
            elif ((1 <= int(s[i-2:i]) <= 26) and (1 <= int(s[i-2]) <= 2)):
                dp[i] = dp[i-2]
             
        
        print(dp) 
        return dp[-1]
