import collections
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d1=collections.Counter(nums1)
        d2=collections.Counter(nums2)
        res=[]
        for k in d2.keys():
            for i in range(min(d1[k],d2[k])):
                res.append(k)
                
        return res
