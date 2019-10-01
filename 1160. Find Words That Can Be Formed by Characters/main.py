class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def s2l(s):
            d = [0]*26
            for e in s:
                d[ord(e) - 97] += 1
            return d
        
        def diff(d, d_):
            for i in range(26):
                d[i] = d[i] - d_[i]
            return d
        
        res = 0
        for word in words:
            t = diff(s2l(chars), s2l(word))
            #print(t)
            if min(t) >= 0:
                res += len(word)
        
        return res
