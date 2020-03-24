from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        res = 0
        d = defaultdict(list)
        for i in range(len(reservedSeats)):
            row, col = reservedSeats[i]
            d[row].append(col)
        res = 2 * (n - len(d))
        for k in d:
            taken = False
            if ((2 not in d[k]) and (3 not in d[k]) and (4 not in d[k]) and (5 not in d[k])):
                taken = True
                res += 1
            if ((6 not in d[k]) and (7 not in d[k]) and (8 not in d[k]) and (9 not in d[k])):
                taken = True
                res += 1
            if ((4 not in d[k]) and (5 not in d[k]) and (6 not in d[k]) and (7 not in d[k])) and not taken:
                res += 1
        return res
