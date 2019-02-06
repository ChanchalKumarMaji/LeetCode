class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d={}
        l=len(s)
        for i in range(l-10+1):
            k=s[i:i+10]
            if k not in d.keys():
                d[k]=1
            else:
                d[k]+=1
        r=[]
        for k in d.keys():
            if d[k]>1:
                r.append(k)
                
        return r
