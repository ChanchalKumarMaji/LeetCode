class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        v = [0] * (n+1)
        v[rounds[0]] += 1
        for i in range(1, len(rounds)):
            s, e = rounds[i-1], rounds[i]
            if s <= e:
                for j in range(s+1, e+1):
                    v[j] += 1
            else:
                for j in range(s+1, n+1):
                    v[j] += 1
                for j in range(1, e+1):
                    v[j] += 1
        #print(v)
        res = []
        m = max(v)
        for i, val in enumerate(v):
            if val == m:
                res.append(i)
        res.sort()
        return res
