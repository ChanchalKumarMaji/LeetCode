class Solution:
    def minFlips(self, target: str) -> int:
        cur = '1'
        count = 0
        for i, c in enumerate(target):
            if c == cur:
                count += 1
                cur = chr(48 + (ord(cur)+1)%2)
        return count
