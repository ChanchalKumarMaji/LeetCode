class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def help(s1, s2):
            res = ''
            for i in range(min(len(s1), len(s2))):
                if s1[i] == s2[i]:
                    res += s1[i]
                else:
                    break 
            return res
        
        if not strs:
            return ''
        res = strs[0]
        for j in range(1, len(strs)):
            res = help(res, strs[j])
        return res
