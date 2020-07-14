class Solution:
    def numSub(self, s: str) -> int:
        res = 0
        count = 0
        p = 10**9 + 7
        for c in s:
            if c == '1':
                count += 1
            else:
                res += count*(count+1) // 2
                res = res % p
                count = 0
        res += count*(count+1) // 2
        return res % p
