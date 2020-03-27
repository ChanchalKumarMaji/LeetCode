class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            i = 1
            c = 0
            s = 0
            while i * i <= num and c <= 4:
                if num % i == 0:
                    if num // i  == i:
                        c += 1
                        s += i
                    else:
                        c += 2
                        s += i + num//i
                i += 1
            if c == 4:
                res += s
        return res
