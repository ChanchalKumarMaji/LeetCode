class Solution:
    def n_digits(self, n):
        c = 0
        while n != 0:
            n = n // 10
            c += 1
        return c
        
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            if self.n_digits(num) % 2 == 0:
                res += 1
        return res
