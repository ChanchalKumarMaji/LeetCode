class Solution:
    def check(self, x, y):
        if len(x) > len(y):
            return False
        for i in range(len(y)):
            if y[i:i+len(x)] == x:
                return True
        return False
    
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        res = set()
        for i in range(n):
            for j in range(n):
                if i != j:
                    x, y = words[i], words[j]
                    if self.check(x, y):
                        res.add(x)
        return list(res)
