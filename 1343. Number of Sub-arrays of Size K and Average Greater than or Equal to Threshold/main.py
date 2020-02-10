class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        res = 0
        s = [0]*(n+1)
        for i in range(n):
            s[i+1] = s[i] + arr[i]
        #print(s)
        for i in range(k, n+1):
            if s[i]-s[i-k] >= k*threshold:
                res += 1
        return res
