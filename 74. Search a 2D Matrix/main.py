class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        l = []
        for e in matrix:
            if len(e) == 0:
                return False
            if e[0] <= target <= e[-1]:
                l[:] = e
                break
        print(l)    
        
        low = 0
        high = len(l) - 1
        
        while low<=high:
            mid = (low+high)//2
            if l[mid] == target:
                return True
            elif l[mid] < target:
                low = mid + 1
            elif l[mid] > target:
                high = mid - 1
                
        return False
