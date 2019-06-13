class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key = operator.itemgetter(1))
        #print(pairs)
        count=1
        pre=pairs[0][1]
        for i in range(1,len(pairs)):
            cur=pairs[i][0] 
            if pre<cur:
                count+=1
                pre=pairs[i][1]
                
        return count
