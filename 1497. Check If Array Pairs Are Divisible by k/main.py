class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d = collections.defaultdict(int)
        for e in arr:
            d[e % k] += 1
        for i in range(len(arr)):
            r = arr[i] % k
            if 2 * r == k:
                if d[r] % 2 != 0:
                    return False
            elif r == 0:
                if d[r] & 1:
                    return False
            elif d[r] != d[k-r]:
                return False
        return True
