import collections
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        d=collections.defaultdict(int)
        for s in S:
            d[s]+=1
        sum=0
        for j in J:
            sum+=d[j]
            
        return sum
