import collections
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d=collections.Counter(nums)
        l=[]
        for key in d.keys():
            l.append((-1*d[key],key))
        
        l.sort()
        #print(l)
        res=[]
        for i in range(k):
            res.append(l[i][1])
        
        return res
