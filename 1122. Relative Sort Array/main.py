class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {}
        for e in arr2:
            d[e] = 0
        for i in range(len(arr1)):
            if arr1[i] in d.keys():
                d[arr1[i]] += 1
                arr1[i] = 0
        arr1.sort()
        i = 0
        for e in arr2:
            for k in range(d[e]):
                arr1[i] = e
                i += 1
                
        return arr1
