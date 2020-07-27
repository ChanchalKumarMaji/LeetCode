class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        temp = [1, 0]
        res = 0
        val = 0
        for i in range(n):
            val = ((val + arr[i]) % 2 + 2) % 2
            temp[val] += 1
        res = temp[0] * temp[1]
        return res % (10**9 + 7)
