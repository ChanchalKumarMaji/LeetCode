import collections
class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d=collections.defaultdict(int)
        l=[] 
        for num in nums:
            if d[num]==1:
                l.append(num)
            else:
                d[num]+=1
        
       
        
        return l
