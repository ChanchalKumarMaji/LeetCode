class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        W = int(math.sqrt(area)) 
        
        for w in range(W, 0, -1):
            if area%w == 0:
                return [area//w , w]
