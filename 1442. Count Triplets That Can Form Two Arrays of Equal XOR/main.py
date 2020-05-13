class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        cache = [0] * (n+1)
        for i in range(n):
            cache[i+1] = cache[i] ^ arr[i]
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j, n):
                    a = cache[j] ^ cache[i]
                    b = cache[k+1] ^ cache[j]
                    if a == b:
                        res += 1
        return res
