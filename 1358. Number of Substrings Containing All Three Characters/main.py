class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        a, b, c = 0, 0, 0
        for i in range(len(s)):
            if s[i] == 'a':
                a = i + 1
                res += min(b, c)
            elif s[i] == 'b':
                b = i + 1
                res += min(a, c)
            else:
                c = i + 1
                res += min(a, b)
        return res
