class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def can_be_extended_to_solution(perm):
            i = len(perm) - 1
            for j in range(i):
                if i - j == abs(perm[i] - perm[j]):
                    return False
            return True

        p = []
        
        def extend(perm, n):
            if len(perm) == n:
                res = [['.' for i in range(n)] for j in range(n)]
                for i in range(n): 
                    res[i][perm[i]] = 'Q' 
                
                l = []
                for i in range(len(res)):
                    l.append("".join(res[i]))
                p.append(l)

            for k in range(n):
                if k not in perm:
                    perm.append(k)

                    if can_be_extended_to_solution(perm):
                        extend(perm, n)

                    perm.pop()
                    
        extend([], n)
        
        return p
