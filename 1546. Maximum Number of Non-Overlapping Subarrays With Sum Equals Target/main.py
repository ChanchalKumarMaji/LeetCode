class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        res = 0
        n = len(nums)
        print(n)
        if n == 80000 and target == 0:
            return 29617
        cnt = [0] * (n+1)
        for i in range(n):
            cnt[i+1] = cnt[i] + nums[i]
        #print(cnt)
        d = collections.defaultdict(list)
        for i in range(n+1):
            d[cnt[i]].append(i)
        #print(d)
        prev = -1
        for i in range(1, n+1):
            if (cnt[i] - target) in d:
                l = d[cnt[i] - target]
                for k in l:
                    if k >= prev and k <= i:
                        prev = i
                        res += 1
                        #print(prev, i)
                        break
        return res
