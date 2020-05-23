class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        res = []
        favoriteCompanies = [set(i) for i in favoriteCompanies]
        n = len(favoriteCompanies)
        for i in range(n):
            f = True
            for j in range(n):
                if i == j:
                    continue
                s1 = set(favoriteCompanies[i])
                s2 = set(favoriteCompanies[j])
                if s1.issubset(s2):
                    f = False
                if not f:
                    break
            if f:
                res.append(i)
        return sorted(res)
