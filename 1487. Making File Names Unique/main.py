class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        res = []
        d = collections.defaultdict(int)
        for name in names:
            if name in d:
                i = d[name] + 1
                while name+"({})".format(i) in d:
                    i += 1
                    d[name] = i
                t = name + "({})".format(i)
                d[t] = 0
                res.append(t)
            else:
                d[name] = 0
                res.append(name)
        return res
