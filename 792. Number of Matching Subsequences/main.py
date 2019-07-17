class Solution:
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        d = {}
        for i in range(26):
            d[chr(97+i)] = []
        
        for word in words:
            d[word[0]].append(word) 
            
        #print(d)
        
        for c in S: 
            new = []
            old = d[c]
            d[c] = []
            for e in old: 
                if len(e)>=2: 
                    new.append(e[1:])
            for e in new:
                d[e[0]].append(e) 
                    
                    
        res = 0            
        for l in d.values():
            res += len(l)
        
        return len(words) - res
