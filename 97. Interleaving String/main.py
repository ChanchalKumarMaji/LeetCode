class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1)+len(s2) != len(s3):
            return False
        
        s1 = [None] + list(s1)
        s2 = [None] + list(s2)
        
        dp = [[0 for j in range(len(s2))] for i in range(len(s1))] 
        
        dp[0][0] = 1
        for j in range(1, len(s2)):
            if s2[j] == s3[j-1]:
                dp[0][j] = dp[0][j-1]
            
        for i in range(1, len(s1)):
            if s1[i] == s3[i-1]: 
                dp[i][0] = dp[i-1][0]
            
        for i in range(1, len(s1)):
            for j in range(1, len(s2)):
                if s1[i] == s3[i+j-1] and s2[j] != s3[i+j-1]:
                    dp[i][j] = dp[i-1][j] 
                elif s2[j] == s3[i+j-1] and s1[i] != s3[i+j-1]: 
                    dp[i][j] = dp[i][j-1] 
                elif s1[i] == s3[i+j-1] and s2[j] == s3[i+j-1]:
                    dp[i][j] = dp[i-1][j] | dp[i][j-1]
                    
                
        
        #print(dp)
        
        if dp[-1][-1]:
            return True
        else:
            return False
