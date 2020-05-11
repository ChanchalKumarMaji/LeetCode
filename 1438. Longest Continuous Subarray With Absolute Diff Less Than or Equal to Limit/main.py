class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0
        bs, be = 0, 0
        mind, maxd = collections.deque([]), collections.deque([])
        s, e = 0, 0
        while e < len(nums):
            x = nums[e]
            while mind and nums[mind[-1]] >= x:
                _ = mind.pop()
            mind.append(e)
            while maxd and nums[maxd[-1]] <= x:
                _ = maxd.pop()
            maxd.append(e)
            minIdx = mind[0]
            minVal = nums[minIdx]
            maxIdx = maxd[0]
            maxVal = nums[maxIdx]
            if maxVal - minVal > limit:
                s += 1
                if s > mind[0]:
                    _ = mind.popleft()
                if s > maxd[0]:
                    _ = maxd.popleft()
            else:
                if e - s + 1 > res:
                    res = e - s + 1
                    bs = s
                    be = e
                e += 1
        return res
