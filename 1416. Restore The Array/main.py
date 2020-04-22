class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        t = len(str(k))
        count = [0] * (n+1)
        count[0] = 1
        count[1] = 1
        for i in range(1, n):
            for j in range(t):
                if i-j >= 0 and int(s[i-j:i+1]) <= k and s[i-j] != "0":
                    count[i+1] += count[i-j]
        return count[-1] % 1000000007
