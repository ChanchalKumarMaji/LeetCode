class Solution:
    def check(self, s):
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                return False
        return True
    
    def strings(self, prefix, n):
        if n == 0:
            if self.check(prefix):
                self.s.append(prefix)
            return
        for c in ['a', 'b', 'c']:
            self.strings(prefix+c, n-1)
    
    def getHappyString(self, n: int, k: int) -> str:
        self.s = []
        self.strings("", n)
        #print(self.s)
        self.s.sort()
        if len(self.s) < k:
            return ""
        return self.s[k-1]
