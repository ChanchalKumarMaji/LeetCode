import collections
class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        d=collections.defaultdict(int)
        
        for i in cpdomains:
            n,s=i.split(' ')
            n=int(n)
            d[s]+=n 
            for j in range(len(s)-1,-1,-1):
                if s[j]=='.':
                    t=s[j+1::]
                    d[t]+=n
        l=[]            
        for k in d.keys():
            l.append(str(d[k])+' '+k)
            
        return l
