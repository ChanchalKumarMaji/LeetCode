class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        n = min(max(target), n)
        for i in range(1, n+1):
            if i in target:
                res += ["Push"]
            else:
                res += ["Push","Pop"]
        return res
