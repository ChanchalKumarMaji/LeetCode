from collections import defaultdict
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        
        for k in d.keys():
            for i in range(d[k] - 1):
                nums.remove(k)
