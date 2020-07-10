class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        if len(S) == 0:
            return []
        res = []
        prev = S[0]
        l = 0
        r = 0
        S = S + "#"
        for i in range(1, len(S)):
            if S[i] == prev:
                r += 1
            else:
                if r-l+1 >= 3:
                    res.append([l, r])
                prev = S[i]
                l = r = i
        return res
