class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        sub=[]
        for i in range(2**n):
            #l=[0 for k in range(n)]
            k=i
            p=[]
            for j in range(n):
                if (k & 1):
                    p.append(nums[j])
                k>>=1
                
            sub.append(p)
            
        return sub
