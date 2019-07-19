class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        d = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = [] 
        for word in words:
            t = ""
            for c in word:
                t += d[(ord(c)-97)]
            res.append(t)    
            
        #print(res)
        
        return len(set(res))
