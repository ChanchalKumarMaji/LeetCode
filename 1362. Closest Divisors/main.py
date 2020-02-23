import math

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        num1 = num + 1
        num2 = num + 2
        diff = float('inf')
        for i in range(1, int(math.sqrt(num2))+1):
            if num1 % i == 0:
                if diff > abs(i - num1//i):
                    diff = abs(i - num1//i)
                    res = [i, num1//i]
            if num2 % i == 0:
                if diff > abs(i - num2//i):
                    diff = abs(i - num2//i)
                    res = [i, num2//i]
        
        return res
