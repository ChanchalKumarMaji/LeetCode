class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts=collections.Counter(nums)
        return max(counts.keys(),key=counts.get)
