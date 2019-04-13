class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counter = 0
        
        i = 0
        
        for j in range(len(t)): 
            if counter<len(s) and s[i]==t[j]: 
                counter += 1
                i += 1
                
                
        return counter==len(s)
