from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        dist = [-1] * n
        q = deque([start])
        dist[start] = 1
        while len(q) > 0:
            u = q.popleft()
            if arr[u] == 0:
                return True
            for k in [-1, 1]:
                v = u + k*arr[u]
                if 0 <= v < n and dist[v] == -1:
                    dist[v] = 1
                    q.append(v)
        return False
