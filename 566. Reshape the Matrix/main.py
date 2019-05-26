class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        matrix=[] 
        for i in nums:
            for j in i:
                matrix.append(j)
        
        list=[]
        k=0
        if len(matrix)==r*c:
            for i in range(r):
                l=[] 
                for j in range(c):
                    l.append(matrix[k])
                    k+=1
                list.append(l)    
        else:
            return nums
        
        return list
