import collections
class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s=0
        c=0
        
        d=collections.defaultdict(int)
        d[0]=1
        for num in nums:
            s+=num
            if s-k in d.keys():
                c=c+d[s-k]
            d[s]+=1
            
        return c
