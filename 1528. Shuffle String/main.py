class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        res = [''] * n
        for i, c in enumerate(s):
            res[indices[i]] = c
        return ''.join(res)
