class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        m=0
        #nums.append(-1) 
        for num in nums:
            if num==1:
                c+=1
            else:
                m=max(m,c)
                c=0
        
        return max(m,c)
