import collections
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        i, j = 0, 0
        d = collections.defaultdict(int) 
        l = 0
        while j < len(s):
            if d[s[j]] == 0:
                d[s[j]] = 1
                l = max(j-i+1, l)
            else:
                while i<=j:
                    if s[j] == s[i]:
                        break
                    else:
                        d[s[i]] = 0
                        i += 1
                i += 1
            j += 1
                 
        return l
