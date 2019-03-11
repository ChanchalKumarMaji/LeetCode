class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counts=collections.Counter(nums)
        l=[]
        for k in counts.keys():
            if counts[k]==1:
                l.append(k)
              
        return l
