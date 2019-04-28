import collections
class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d=collections.Counter(s)
        l=[]
        for k in d.keys():
            l.append((d[k],k))
        l.sort()
        k=len(l)
        st=''
        for i in range(k-1,-1,-1):
            for j in range(l[i][0]):
                st=st+l[i][1]
                
        return st
