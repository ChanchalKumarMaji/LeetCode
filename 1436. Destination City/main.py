class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        return list(set(itertools.chain(*paths)) - set(itertools.chain(path[0] for path in paths)))[0]
