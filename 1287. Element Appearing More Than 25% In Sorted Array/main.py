class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr) // 4
        c = 0
        prev = -1
        for e in arr:
            if e == prev:
                c += 1
            else:
                c = 1
            prev = e
            if c > n:
                return e
