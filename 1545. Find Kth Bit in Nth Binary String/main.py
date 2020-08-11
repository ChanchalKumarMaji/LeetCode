class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s1 = '0'
        def convert(s):
            res = ''
            for c in s:
                if c == '0':
                    res += '1'
                else:
                    res += '0'
            return res[::-1]
        for _ in range(n-1):
            si = s1 + '1' + convert(s1)
            s1 = si
        return s1[k-1]
