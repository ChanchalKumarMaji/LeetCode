class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        p = float('-inf')
        for i, num in enumerate(nums):
            c = 0
            m = 0
            while num > 0:
                if num % 2 == 0:
                    num = num // 2
                    m += 1
                else:
                    num -= 1
                    c += 1
            p = max(p, m)
            res += c
        return res + p
