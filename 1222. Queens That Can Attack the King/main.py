class Solution:    
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:       
        dr = [1, -1, 0, 0, 1, -1, 1, -1]
        dc = [0, 0, 1, -1, 1, 1, -1, -1]
        res = []
        for d in range(8):
            r, c = king
            x, y = dr[d], dc[d]
            for _ in range(7):
                r += x
                c += y
                if [r, c] in queens:
                    res.append([r, c])
                    break
                
        return res
