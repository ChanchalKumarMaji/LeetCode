class Solution:
    def isHappy(self, n: 'int') -> 'bool':
        s = set()
        while n != 1:
            n = sum([int(e)**2 for e in str(n)])
            if n in s:
                return False
            s.add(n)
        return True
