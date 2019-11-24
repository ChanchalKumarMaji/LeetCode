class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        globalMin = 10000000
        for i in range(1, len(arr)):
            globalMin = min(globalMin, arr[i]-arr[i-1])
        res = []
        for i in range(1, len(arr)):
            if arr[i]-arr[i-1] == globalMin:
                res.append([arr[i-1], arr[i]])
                
        return res
