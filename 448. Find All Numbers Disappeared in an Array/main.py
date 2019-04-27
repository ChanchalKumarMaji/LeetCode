class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        for i in range(len(nums)): 
            if nums[i]!='#':
                j=nums[i]-1
                while nums[j]!='#':
                    n=nums[j]-1
                    nums[j]='#'
                    j=n
        
        
                
        return [i+1 for i in range(len(nums)) if nums[i]!='#']
