class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r = 0
        l = 0
        res = 0
        for i in range(len(s)):
            if s[i] == 'L':
                l += 1
            elif s[i] == 'R':
                r += 1
                
            if l == r:
                res += 1
                l = 0
                r = 0
        
        return res
