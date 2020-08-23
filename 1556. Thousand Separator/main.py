class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)[::-1]
        s = ""
        for i in range(0, len(n), 3):
            s += n[i : i+3] + '.'
        return s[:-1][::-1]
