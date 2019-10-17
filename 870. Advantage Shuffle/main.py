from collections import defaultdict 

class Solution:
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        a = []
        b = []
        a[:], b[:] = A, B
        
        a.sort()
        b.sort() 
        
        rem = []
        d = defaultdict(list) 
        i, j = 0, 0
        
        while i<len(a) and j<len(b): 
            if a[i] > b[j]:
                d[b[j]].append(a[i]) 
                i += 1
                j += 1
            else:
                rem.append(a[i]) 
                i += 1
                
        #print(d) 
        #print(rem) 
        res = []
        for i in range(len(B)): 
            if B[i] in d and len(d[B[i]])>0: 
                l = d[B[i]]
                res.append(l[-1]) 
                l.remove(l[-1])  
                d[B[i]] = l
            else:
                res.append(rem[-1])
                rem.remove(rem[-1]) 
         
            
        return res
