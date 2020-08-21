class Solution:
    def minOperations(self, n: int) -> int:
        return sum([abs(n - (2*i + 1)) for i in range(n)]) // 2
