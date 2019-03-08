class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        h=[0 for i in range(26)]
        for k in s:
            h[ord(k)-97]+=1
        for k in t:
            h[ord(k)-97]-=1
        for p in h:
            if p!=0:
                return False
            
        return True
