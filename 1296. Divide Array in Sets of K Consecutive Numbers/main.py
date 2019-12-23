from collections import defaultdict
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        for key in sorted(d.keys()):
            for _ in range(d[key]):
                for i in range(k):
                    if key+i in d.keys():
                        d[key+i] -= 1
                    else:
                        return False
        
        return True
