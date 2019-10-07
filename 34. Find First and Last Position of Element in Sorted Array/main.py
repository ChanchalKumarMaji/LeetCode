class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        low = 0
        high = len(nums) - 1
        f = 0
        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                f = 1
                break
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
                
        i, j = mid, mid
        
        while i>=1 and nums[i-1] == target:
            i = i-1
        while j<len(nums)-1 and nums[j+1] == target:
            j = j+1
        
        if f == 1:
            return [i, j]
        else:
            return [-1, -1]

        
