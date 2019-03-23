import collections
class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        num=[]
        
        d=collections.defaultdict(int)
        
        for word in words:
            v=[0 for i in range(26)]
            for c in word:
                v[ord(c)-97]=1
            n=0
            for i in range(26):
                n+=pow(2,25-i)*v[i]
            num.append(n)         
        
        m=0
        
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if (num[i] & num[j])==0:
                    m=max(m,len(words[i])*len(words[j]))
            
        return m
