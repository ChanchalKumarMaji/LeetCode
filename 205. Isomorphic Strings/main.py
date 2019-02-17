class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        return len(set(zip(s,t)))==len(set(s))==len(set(t))
