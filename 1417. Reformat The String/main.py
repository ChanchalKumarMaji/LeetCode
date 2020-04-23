class Solution:
    def reformat(self, s: str) -> str:
        c = []
        d = []
        for e in s:
            if e.isdigit():
                d.append(e)
            else:
                c.append(e)
        if abs(len(c) - len(d)) > 1:
            return ""
        res = ""
        if len(c) > len(d):
            res = c[0]
            for i in range(len(d)):
                res += d[i] + c[i+1]
        elif len(c) < len(d):
            res = d[0]
            for i in range(len(c)):
                res += c[i] + d[i+1]
        else:
            for i in range(len(c)):
                res += c[i] + d[i]
        return res
