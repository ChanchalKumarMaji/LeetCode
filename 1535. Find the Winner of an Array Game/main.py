class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
        q = collections.deque(arr)
        c = 0
        w = q[0]
        while c != k:
            a, b = max(q[0], q[1]), min(q[0], q[1])
            q.popleft()
            q.popleft()
            if a == w:
                c += 1
            else:
                c = 1
                w = a
            q.appendleft(a)
            q.append(b)
        return w
