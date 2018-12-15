class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        n0=0
        n1=0
        n2=0
        
        for e in nums:
            if e==0:
                n0+=1
            elif e==1:
                n1+=1
            else:
                n2+=1
                
        for i in range(n0):
            nums[i]=0
        for i in range(n0,n0+n1):
            nums[i]=1
        for i in range(n0+n1,n0+n1+n2):
            nums[i]=2
