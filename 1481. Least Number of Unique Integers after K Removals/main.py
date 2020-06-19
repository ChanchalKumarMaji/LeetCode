class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = collections.Counter(arr)
        l = list(zip(d.values(), d.keys()))
        l.sort()
        p = []
        for (a, b) in l:
            p += [b] * a
        return len(set(p[k:]))
