from collections import deque

class Solution:
    def check(self, s1, s2):
        count = 0
        for i in range(8):
            if s1[i] != s2[i]:
                count += 1
        return count == 1
    
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1
        bank.append(start)
        bank = list(set(bank))
        n = len(bank)
        AdjList = [[] for _ in range(n)]
        for i in range(0, n-1):
            for j in range(i+1, n):
                if self.check(bank[i], bank[j]):
                    AdjList[i].append(j)
                    AdjList[j].append(i)
        s, e = -1, -1
        for i in range(n):
            if bank[i] == start:
                s = i
            if bank[i] == end:
                e = i
        q = deque([s])
        dist = [-1] * n
        dist[s] = 0
        while len(q) != 0:
            u = q.popleft()
            for j in range(len(AdjList[u])):
                v = AdjList[u][j]
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        
        return dist[e]
