class Solution {
    int dr[4] = {1, 0, -1, 0};
    int dc[4] = {0, 1, 0, -1};
    int R, C;
    vector<vector<char> > grid;
    void floodfill(int r, int c, char c1, char c2){
        if(r<0 || r>=R || c<0 || c>=C)
            return;
        if(grid[r][c] != c1)
            return;
        grid[r][c] = c2;
        for(int d=0; d<4; d++){
            floodfill(r+dr[d], c+dc[d], c1, c2);
        }
    }
        
public:
    void solve(vector<vector<char>>& board) {
        if(board.size() == 0)
            return;
        R = board.size();
        C = board[0].size();
        grid = board;
        for(int i=0; i<C; i++){
            if(grid[0][i] == 'O')
                floodfill(0, i, 'O', '#');
            if(grid[R-1][i] == 'O')
                floodfill(R-1, i, 'O', '#');
        }
        for(int i=1; i<R-1; i++){
            if(grid[i][0] == 'O')
                floodfill(i, 0, 'O', '#');
            if(grid[i][C-1] == 'O')
                floodfill(i, C-1, 'O', '#'); 
        }
        for(int i=0; i<R; i++){
            for(int j=0; j<C; j++){
                if(grid[i][j] == 'O')
                    grid[i][j] = 'X';
            }
        }
        for(int i=0; i<R; i++){
            for(int j=0; j<C; j++){
                if(grid[i][j] == '#')
                    grid[i][j] = 'O'; 
            }
        }
        board = grid; 
    }
};
