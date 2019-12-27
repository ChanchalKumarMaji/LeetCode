from collections import defaultdict

class Solution:
    def slidingWindow(self, s, w, maxLetters):
        print(w)
        count = [0] * 256
        num = 0
        for i in range(len(s)):
            c = s[i]
            if count[ord(c)] == 0:
                count[ord(c)] += 1
                num += 1
            else:
                count[ord(c)] += 1
            if i >= w-1:
                if num <= maxLetters:
                    self.d[s[i-w+1:i+1]] += 1
                c = s[i-w+1]
                count[ord(c)] -= 1
                if count[ord(c)] == 0:
                    num -= 1
    
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        self.d = defaultdict(int)
        self.d['#'] = 0
        for w in range(minSize, minSize+1):
            self.slidingWindow(s, w, maxLetters)
        print(self.d)
        return max(self.d.values())
