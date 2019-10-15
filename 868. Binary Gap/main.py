class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = bin(N)
        res = 0
        i = 0
        while i<len(s):
            if s[i]=='1':
                break 
            i += 1
        pre = i    
        for i in range(pre+1, len(s)):
            if s[i]=='1':
                res = max(res, i-pre)
                pre = i
                
        return res
