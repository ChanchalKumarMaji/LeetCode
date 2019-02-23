class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d={}
        l=len(nums)
        for i in range(l):
            if nums[i] not in d.keys():
                d[nums[i]]=[i]
            else:
                d[nums[i]].append(i)
                
        for t in d.keys():
            if len(d[t])>1:
                for i in range(len(d[t])-1):
                    if d[t][i+1]-d[t][i]<=k:
                        return True
                
        return False
