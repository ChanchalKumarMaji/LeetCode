class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        for i in range(n-m*k+1):
            nums = arr[i:i+m*k]
            #print(nums)
            s = set()
            for i in range(0, len(nums), m):
                s.add(tuple(nums[i:i+m]))
            if len(s) == 1:
                return True
        return False
