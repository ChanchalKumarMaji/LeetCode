class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[1 for j in range(n)] for i in range(n)] 
        
        l = 1
        t = s[0] 
        
        for i in range(1, n):
            p = i
            for j in range(n-i): 
                if s[j] != s[p]:
                    dp[j][p] = 0
                else:
                    dp[j][p] = dp[j+1][p-1]
                    if dp[j][p] == 1:
                        l += 2
                        t = s[j:p+1]
                
                p += 1
                
        return t
