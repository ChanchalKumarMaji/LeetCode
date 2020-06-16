class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        count = [0] * (n + 1)
        for i in range(n):
            count[i+1] = count[i] + arr[i]
        d = collections.defaultdict(int)
        d[0] = 0
        h = []
        for r in range(1, n+1):
            if count[r]-target in d:
                l = d[count[r]-target]
                h.append((l+1, r))
            d[count[r]] = r
        h.sort(key = lambda x : (x[1]-x[0], x[0], x[1]))
        print(h)
        for i in range(len(h)):
            x1, y1 = h[i]
            for j in range(i+1, len(h)):
                x2, y2 = h[j]
                if y1 < x2 or y2 < x1:
                    return y1-x1 + y2-x2 + 2
        return -1
