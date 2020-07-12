class Solution:
    def minimumDeleteSum(self, word1, word2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        
        l1 = [0]
        for w in word1:
            l1.append(w)
        l2 = [0]
        for w in word2:
            l2.append(w)
        
        grid = [[0 for j in range(len(word1)+1)] for i in range(len(word2)+1)]
        
        for i in range(1,len(word2)+1):
            grid[i][0] = ord(l2[i]) + grid[i-1][0]
        for j in range(1,len(word1)+1):
            grid[0][j] = ord(l1[j]) + grid[0][j-1]
        
        for i in range(1,len(word2)+1):
            for j in range(1,len(word1)+1):
                if l2[i] != l1[j]:
                    grid[i][j] = min(grid[i-1][j]+ord(l2[i]) , grid[i][j-1]+ord(l1[j]) ) 
                else:
                    grid[i][j] = grid[i-1][j-1]
                    
        return grid[-1][-1]
