class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        d = {}
        d[5] = 0
        d[10] = 0
        d[20] = 0
        
        for bill in bills:
            if bill == 5:
                d[5] += 1
            elif bill == 10:
                if d[5] >= 1:
                    d[5] -= 1
                    d[10] += 1
                else:
                    return False
            elif bill == 20:
                if d[5] >= 1 and d[10] >= 1:
                    d[5] -= 1
                    d[10] -= 1
                    d[20] += 1
                elif d[5] >= 3:
                    d[5] -= 3
                    d[20] += 1
                else:
                    return False
                
        return True
