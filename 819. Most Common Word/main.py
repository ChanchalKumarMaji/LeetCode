import collections
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        d=collections.defaultdict(int)
        s=''
        paragraph+=" "
        for e in paragraph:
            if e==" " or e=="?" or e=="'" or e=="," or e==";" or e=="." or e=="!":
                s=s.lower()
                if s not in banned:
                    d[s]+=1
                s=''
            else:
                s=s+e
        m=0
        for k in d.keys():
            if d[k]>m and k!="":
                m=d[k]
                s=k
                
        return s
