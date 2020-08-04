class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        d = collections.defaultdict(int)
        z = [0] * m
        for i in range(m):
            for j in range(n-1, -1, -1):
                if grid[i][j] == 0:
                    z[i] += 1
                else:
                    break
        res = 0
        for r in range(n-1, 0, -1):
            print(z)
            f = True
            for i in range(len(z)):
                if z[i] >= r:
                    res += i
                    z[:] = z[:i] + z[i+1:]
                    f = False
                    break
            if f:
                return -1
        return res
