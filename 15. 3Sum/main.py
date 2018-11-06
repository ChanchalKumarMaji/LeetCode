class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort() 
        res=[]
        for k in range(len(nums)-2):
            if k>0 and nums[k]==nums[k-1]:
                continue
            l=k+1
            r=len(nums)-1
            while (l<r):
                s=nums[k]+nums[l]+nums[r]
                if s>0:
                    r=r-1
                elif s<0:
                    l=l+1
                else:
                    res.append([nums[k],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l=l+1
                    while l<r and nums[r]==nums[r-1]:
                        r=r-1
                    l=l+1
                    r=r-1
                
                    
        return res
