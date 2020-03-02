class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        d = {}
        for vote in votes:
            for i in range(len(vote)):
                if vote[i] not in d:
                    d[vote[i]] = [0]*26
                    d[vote[i]][i] -= 1
                else:
                    d[vote[i]][i] -= 1
        res = []
        for k in d:
            res.append((d[k], k))
        res.sort()
        
        return ''.join([e[1] for e in res])
