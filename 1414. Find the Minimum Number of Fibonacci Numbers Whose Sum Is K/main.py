class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibo = [0, 1, 1]
        while True:
            n = fibo[-1] + fibo[-2]
            if n > k:
                break
            fibo.append(n)
        count = 0
        j = len(fibo) - 1
        while k > 0:
            count += k // fibo[j]
            k = k % fibo[j]
            j -= 1
        return count
