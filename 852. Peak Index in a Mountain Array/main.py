class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(2, len(A)):
            if A[i-2] < A[i-1] > A[i]:
                return i-1
