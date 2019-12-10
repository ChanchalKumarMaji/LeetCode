class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if upper + lower != sum(colsum):
            return []
        n = len(colsum)
        res = [[0]*n for _ in range(2)]
        c_2 = 0
        for i in range(n):
            if colsum[i] == 2:
                res[0][i], res[1][i] = 1, 1
                c_2 += 1
        
        if c_2 > upper or c_2 > lower:
            return []
        
        u, l = upper-c_2, lower-c_2
        
        for i in range(n):
            if colsum[i] == 1:
                if u > 0:
                    res[0][i] = 1
                    u -= 1
                elif l > 0:
                    res[1][i] = 1
                    l -= 1
        
        return res
