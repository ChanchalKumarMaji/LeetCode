import collections
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d=collections.OrderedDict()
        l=len(s)
        for i in range(l):
            if s[i] not in d.keys():
                d[s[i]]=i
            else:
                d[s[i]]=-1
                
        for k in d.keys():
            if d[k]!=-1:
                return d[k]
            
        return -1
