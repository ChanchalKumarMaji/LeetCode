class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        l=[]
        for i in range(len(nums)):
            l.append((-1*nums[i],i))
        res=["" for i in range(len(nums))]    
        l.sort()
        #print(l)
        res[l[0][1]]="Gold Medal"
        if len(l)==1:
            return res
        res[l[1][1]]="Silver Medal"
        if len(l)==2:
            return res
        res[l[2][1]]="Bronze Medal"
        i=3
        while i<len(l):
            res[l[i][1]]=str(i+1) 
            i+=1 
        return res
