from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        d = defaultdict(list)
        for i in range(n):
            d[arr[i]].append(i)
        q = deque([0])
        dist = [-1]*n
        dist[0] = 0
        while q:
            u = q.popleft()
            for v in [u-1, u+1] + d[arr[u]][::-1]:
                if 0 <= v < n and u != v and dist[v] == -1:
                    dist[v] = dist[u] + 1
                    if v == n-1:
                        return dist[v]
                    q.append(v)
        return dist[n-1]
