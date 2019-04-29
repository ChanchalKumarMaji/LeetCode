class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if not s:
            return 0
        
        g.sort()
        s.sort()
        
        res = 0
        
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                res += 1
                i += 1 
            j += 1
                
        return res
