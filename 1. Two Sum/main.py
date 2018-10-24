class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        l=len(nums)
        for i in range(l):
            if target-nums[i] not in d.keys():
                d[nums[i]]=i
            else:
                break
                
        l=[i,d[target-nums[i]]]
        #l.sort()

            
        
        return l
