class Solution:
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        while p%2==0 and q%2==0:
            p = p//2
            q = q//2
        return 1 - p%2 + q%2
