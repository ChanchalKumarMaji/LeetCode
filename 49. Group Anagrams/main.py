class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d=collections.defaultdict(list)
        for s in strs:
            d[''.join(sorted(s))].append(s)
            
        return list(d.values())
