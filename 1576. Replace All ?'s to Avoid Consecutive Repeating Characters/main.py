class Solution:
    def give(self, c1, c2):
        chrs = 'abcdefghijklmnopqrstuvwxyz'
        for c in chrs:
            if c != c1 and c != c2:
                return c
    
    def modifyString(self, s: str) -> str:
        s = '#' + s + '#'
        s = list(s)
        for i in range(1, len(s)-1):
            if s[i] == '?':
                c = self.give(s[i-1], s[i+1])
                s[i] = c
        return ''.join(s[1:-1])
