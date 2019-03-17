class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        r=len(board)
        c=len(board[0])
        
        matrix=[[0 for j in range(c)] for i in range(r)]
        
        for i in range(r):
            for j in range(c):
                count=0
                if i-1>=0 and board[i-1][j]==1:
                    count+=1
                if i-1>=0 and j-1>=0 and board[i-1][j-1]==1:
                    count+=1
                if i-1>=0 and j+1<c and board[i-1][j+1]==1:
                    count+=1
                if i+1<r and board[i+1][j]==1:
                    count+=1
                if j-1>=0 and board[i][j-1]==1:
                    count+=1
                if j+1<c and board[i][j+1]==1:
                    count+=1
                if i+1<r and j-1>=0 and board[i+1][j-1]==1:
                    count+=1
                if i+1<r and j+1<c and board[i+1][j+1]==1:
                    count+=1    
                   
                if board[i][j]==1 and count<2:
                    matrix[i][j]=0
                elif board[i][j]==1 and (count==2 or count==3):
                    matrix[i][j]=1
                elif board[i][j]==1 and count>3:
                    matrix[i][j]=0
                elif board[i][j]==0 and count==3:
                    matrix[i][j]=1
                else:
                    matrix[i][j]=0 
                    
        for i in range(r):
            for j in range(c):
                board[i][j]=matrix[i][j]
