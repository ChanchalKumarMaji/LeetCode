from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1, c2 = Counter(s), Counter(t)
        return sum((c1-c2).values())
