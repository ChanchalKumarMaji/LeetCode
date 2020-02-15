from collections import Counter

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = Counter(arr) 
        if d[0] >= 2:
            return True
        for num in arr:
            if (num != 0) and (2 * num in d):
                return True
        return False
