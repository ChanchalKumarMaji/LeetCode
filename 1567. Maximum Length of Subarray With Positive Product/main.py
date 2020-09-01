class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        localMax=1
        a = 0
        localMin=1
        b = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = 0
            elif nums[i] > 0:
                nums[i] = 1
            else:
                nums[i] = -1
        for i in range(len(nums)):
            if nums[i]>0:
                if localMax * nums[i] >= nums[i]:
                    localMax = localMax * nums[i]
                    a += 1
                else:
                    localMax = nums[i]
                    a = 1
                if localMin * nums[i] <= nums[i]:
                    localMin = localMin * nums[i]
                    b += 1
                else:
                    localMin = nums[i]
                    b = 1
            else:
                p = 0
                localMax_ = 0
                if localMin * nums[i] >= nums[i]:
                    localMax_ = localMin * nums[i]
                    p = b + 1
                else:
                    localMax_ = nums[i]
                    p = 1
                if localMax * nums[i] <= nums[i]:
                    localMin = localMax * nums[i]
                    b = a + 1
                else:
                    localMin = nums[i]
                    b = 1
                localMax = localMax_
                a = p
            if localMax > 0:
                res = max(res, a)
        return res
