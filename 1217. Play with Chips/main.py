class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        even, odd = 0, 0
        for chip in chips:
            if chip % 2 == 0:
                even += 1
            else:
                odd += 1
        
        return min(even, odd)
