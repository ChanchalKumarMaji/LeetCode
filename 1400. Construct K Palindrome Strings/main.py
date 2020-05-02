from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        d = Counter(s)
        odd = 0
        for key in d:
            if d[key] % 2 == 1:
                odd += 1
                d[key] -= 1
        if odd > k:
            return False
        even = len(s) - odd
        if even >= k-odd:
            return True
        return False
