from collections import defaultdict, deque

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        res = []
        d = defaultdict(int)
        n = len(watchedVideos)
        dist = [-1]*n
        q = deque([id])
        dist[id] = 0
        while len(q) != 0:
            u = q.popleft()
            for v in friends[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    if dist[v] == level:
                        for e in watchedVideos[v]:
                            d[e] += 1
                    if dist[v] > level:
                        break
                    q.append(v)
        for e in sorted(zip(d.values(), d.keys())):
            res.append(e[1])
        return res
