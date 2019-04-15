import collections
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = collections.Counter(s) 
        print(d)
        
        flag = 0
        res = 0
        for v in d.values():
            if v%2==0:
                res += v
            else:
                flag = 1
                res += v-1
                
        return res if flag==0 else res+1
