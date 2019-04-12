import collections
class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        c=0 
        for e in s+t:
            c=c^ (ord(e)-97)
            
            
            
        return chr(c+97)
