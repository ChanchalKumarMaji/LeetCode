class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<=1:
            return 0
        dp = [0 for i in range(len(s))]
        for i in range(1,len(s)):
            if s[i] == ')':
                if s[i-1]=='(':
                    dp[i] = (dp[i-2] if i-2>=0 else 0) + 2
                elif (i-dp[i-1]-1>=0) and (s[i-dp[i-1]-1]=='('):
                    dp[i] = dp[i-1] + (dp[i-dp[i-1]-2] if (i-dp[i-1]-2>=0) else 0) + 2
                    
        print(dp)
        
        return max(dp)
