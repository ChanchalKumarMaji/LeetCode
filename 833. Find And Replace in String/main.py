class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        res=[c for c in S]
        #print(res)
        for i in range(len(indexes)):
            I=indexes[i]
            s=sources[i]
            t=targets[i]
            if S[I:I+len(s)]==s:
                res[I]=t
                for j in range(1,len(s)):
                    res[I+j]='0'
            
        #print(res)    
        
        p=""
        for e in res:
            if e!='0':
                p=p+e
                
        return p
