import collections
class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        d=collections.Counter(words)
        l=[]
        for key in d.keys():
            l.append((-1*d[key],key)) 
        l.sort()
        res=[]
        for i in range(k):
            res.append(l[i][1])
        return res
