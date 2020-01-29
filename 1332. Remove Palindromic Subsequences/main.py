class Solution:
    def removePalindromeSub(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        if s[:n//2] == s[-(n//2):][::-1]:
            return 1
        else:
            return 2
