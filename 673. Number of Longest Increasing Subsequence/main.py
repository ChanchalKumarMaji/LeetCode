class Solution:
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1 for i in range(len(nums))]
        c = [1 for i in range(len(nums))] 
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    #dp[i] = max(dp[j]+1, dp[i])
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        c[i] = c[j] 
                    elif dp[i] == dp[j] + 1:
                        c[i] += c[j] 
                    
                        
        print(c) 
        print(dp)         
        
        m = max(dp)
        res = 0
        for i in range(len(dp)):
            if dp[i] == m:
                res += c[i]
                
        return res
