class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
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
                p.append(1)

            for k in range(n):
                if k not in perm:
                    perm.append(k)

                    if can_be_extended_to_solution(perm):
                        extend(perm, n)

                    perm.pop()
                    
        extend([], n)
        
        return p.count(1)
