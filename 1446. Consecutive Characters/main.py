class Solution:
    def maxPower(self, s: str) -> int:
        res = 0
        c = 1
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                c += 1
            else:
                res = max(res, c)
                c = 1
        return max(res, c)
