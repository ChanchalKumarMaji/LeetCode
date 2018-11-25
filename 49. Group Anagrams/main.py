class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d=collections.defaultdict(list)
        for s in strs:
            d[''.join(sorted(s))].append(s)
            
        l=[]
        for k in d.values():
            l.append(k)
            
        return l
