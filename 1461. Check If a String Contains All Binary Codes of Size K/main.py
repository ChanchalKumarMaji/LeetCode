class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        s1 = set()
        for i in range(k, len(s)):
            s1.add(s[i-k:i])
        s1.add(s[-k:])
        #print(s1)
        return len(s1) == 2**k
