class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l=nums
        j=0
        for i in range(len(l)):
            if l[i]!=0:
                nums[j]=l[i]
                j+=1
        for k in range(j,len(nums)):
            nums[k]=0
