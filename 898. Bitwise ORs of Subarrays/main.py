class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        ORs = set()
        cur = set()
        for a in A:
            cur = {e | a for e in cur} | {a}
            ORs |= cur
        return len(ORs)
