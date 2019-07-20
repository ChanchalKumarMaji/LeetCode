class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        res=[1,0]
        w=0
        for s in S:
            val=widths[ord(s)-97]
            if w+val>100:
                w=val 
                res[0]+=1
            else:
                w+=val 
                
        res[1]=w
        
        return res
