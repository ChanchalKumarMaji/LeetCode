class Solution:
    def check(self, board):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != '':
                if board[i][0] == 'X':
                    return 'A'
                return 'B'
        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j] != '':
                if board[0][j] == 'X':
                    return 'A'
                return 'B'
        if board[0][0] == board[1][1] == board[2][2] != '':
            if board[0][0] == 'X':
                return 'A'
            return 'B'
        if board[2][0] == board[1][1] == board[0][2] != '':
            if board[2][0] == 'X':
                return 'A'
            return 'B'
        return 'Pending'
        
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [['']*3 for _ in range(3)]
        for i in range(len(moves)):
            x, y = moves[i]
            if i % 2 == 0:
                board[x][y] = 'X'
            else:
                board[x][y] = 'O'
            #print(board)
            k = self.check(board)
            if k != 'Pending':
                return k
        
        if k == 'Pending' and len(moves) == 9:
            return 'Draw'
        return k
