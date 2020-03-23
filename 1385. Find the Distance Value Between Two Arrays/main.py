class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = [1] * len(arr1)
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    res[i] = 0
        return sum(res)
