from collections import deque

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[-1 for j in range(n)] for i in range(m)]
        q = deque([(0, 0)])
        visited[0][0] = 1
        while len(q) != 0:
            #print(q)
            u = q.popleft()
            i, j = u
            visited[i][j] = 1
            if i == m-1 and j == n-1:
                return True
            k = grid[i][j]
            if k == 1:
                if j-1>=0 and visited[i][j-1] == -1 and grid[i][j-1] in [1, 4, 6]:
                    q.append((i, j-1))
                    visited[i][j-1] == 1
                if j+1<n and visited[i][j+1] == -1 and grid[i][j+1] in [1, 3, 5]:
                    q.append((i, j+1))
                    visited[i][j+1] == 1
            elif k == 2:
                if i-1>=0 and visited[i-1][j] == -1 and grid[i-1][j] in [2, 3, 4]:
                    q.append((i-1, j))
                    visited[i-1][j] == 1
                if i+1<m and visited[i+1][j] == -1 and grid[i+1][j] in [2, 5, 6]:
                    q.append((i+1, j))
                    visited[i+1][j] == 1
            elif k == 3:
                if j-1>=0 and visited[i][j-1] == -1 and grid[i][j-1] in [1, 4, 6]:
                    q.append((i, j-1))
                    visited[i][j-1] == 1
                if i+1<m and visited[i+1][j] == -1 and grid[i+1][j] in [2, 5, 6]:
                    q.append((i+1, j))
                    visited[i+1][j] == 1
            elif k == 4:
                if i+1<m and visited[i+1][j] == -1 and grid[i+1][j] in [2, 5, 6]:
                    q.append((i+1, j))
                    visited[i+1][j] == 1
                if j+1<n and visited[i][j+1] == -1 and grid[i][j+1] in [1, 3, 5]:
                    q.append((i, j+1))
                    visited[i][j+1] == 1
            elif k == 5:
                if j-1>=0 and visited[i][j-1] == -1 and grid[i][j-1] in [1, 4, 6]:
                    q.append((i, j-1))
                    visited[i][j-1] == 1
                if i-1>=0 and visited[i-1][j] == -1 and grid[i-1][j] in [2, 3, 4]:
                    q.append((i-1, j))
                    visited[i-1][j] == 1
            elif k == 6:
                if i-1>=0 and visited[i-1][j] == -1 and grid[i-1][j] in [2, 3, 4]:
                    q.append((i-1, j))
                    visited[i-1][j] == 1
                if j+1<n and visited[i][j+1] == -1 and grid[i][j+1] in [1, 3, 5]:
                    q.append((i, j+1))
                    visited[i][j+1] == 1
        return False
