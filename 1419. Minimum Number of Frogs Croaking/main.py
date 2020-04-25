class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        d = collections.defaultdict(int)
        res = 0
        p = [0, 0, 0, 0, 0]
        for c in croakOfFrogs:
            if c == 'c':
                p[0] += 1
            elif c == 'r':
                p[1] += 1
            elif c == 'o':
                p[2] += 1
            elif c == 'a':
                p[3] += 1
            else:
                p[4] += 1
        if not(p[0] == p[1] == p[2] == p[3] == p[4]):
            return -1
        for i in range(len(croakOfFrogs)):
            c = croakOfFrogs[i]
            if c == 'c':
                d['c'] += 1
            elif c == 'r' and ('c' in d) and (d['c'] > 0):
                d['cr'] += 1
                d['c'] -= 1
            elif c == 'o' and ('cr' in d) and (d['cr'] > 0):
                d['cro'] += 1
                d['cr'] -= 1
            elif c == 'a' and ('cro' in d) and (d['cro'] > 0):
                d['croa'] += 1
                d['cro'] -= 1
            elif c == 'k' and ('croa' in d) and (d['croa'] > 0):
                d['croak'] += 1
                d['croa'] -= 1
            else:
                return -1
            res = max(res, sum([d['c'], d['cr'], d['cro'], d['croa']]))
            #print(d)
            
        return res
