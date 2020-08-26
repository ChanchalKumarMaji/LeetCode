class UFDS:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n
        self.sizes = [1] * n
        self.numdisjoint = n

    def find(self, x):
        xp = x
        children = []
        while xp != self.parents[xp]:
            children.append(xp)
            xp = self.parents[xp]
        for c in children:
            self.parents[c] = xp
        return xp

    def union(self, a, b):
        ap = self.find(a)
        bp = self.find(b)
        if ap == bp:
            return

        if self.ranks[ap] < self.ranks[bp]:
            self.parents[ap] = bp
            self.sizes[bp] += self.sizes[ap]
        elif self.ranks[bp] < self.ranks[ap]:
            self.parents[bp] = ap
            self.sizes[ap] += self.sizes[bp]
        else:
            self.parents[bp] = ap
            self.ranks[ap] += 1
            self.sizes[ap] += self.sizes[bp]

        self.numdisjoint -= 1

    def size(self, x):
        return self.sizes[self.find(x)]

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        def coor(i, j):
            return i * n + j
        
        edges = set()
        for i in range(m):
            for j in range(n):
                x = coor(i, j)
                for (dr, dc) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    r, c = i + dr, j + dc
                    if (0 <= r < m) and (0 <= c < n):
                        y = coor(r, c)
                        if grid[i][j] == grid[r][c]:
                            edges.add((min(x, y), max(x, y)))
        #print(edges)
        u = UFDS(m*n)
        for (x, y) in edges:
            if (u.find(x) == u.find(y)) and u.size(x) >= 4:
                return True
            u.union(x, y)
        return False
