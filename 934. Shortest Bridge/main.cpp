class Solution {
    vector<int> dr = vector<int>({1, 0, -1, 0});
    vector<int> dc = vector<int>({0, 1, 0, -1});
    void floodFill(int r, int c, const int R, const int C, vector<vector<int>>& grid){
        if(r<0 || r>=R || c<0 || c>=C) return;
        if(grid[r][c] != 1) return;
        grid[r][c] = 2;
        for(int d=0; d<4; d++){
            floodFill(r+dr[d], c+dc[d], R, C, grid);
        }
    }
    bool extend(int r, int c, int c1, const int R, const int C, vector<vector<int>>& grid){
        for(int d=0; d<4; d++){
            int x = r+dr[d], y = c+dc[d];
            if(x<0 || x>=R || y<0 || y>=C) continue;
            if(grid[x][y] == 0) grid[x][y] = c1;
            if(grid[x][y] == 1) return true;
        }
        return false;
    }
public:
    int shortestBridge(vector<vector<int>>& grid) {
        int R = grid.size(), C = grid[0].size();
        bool f = false;
        for(int i=0; i<R && !f; i++){
            for(int j=0; j<C && !f; j++){
                if(grid[i][j] == 1){
                    floodFill(i, j, R, C, grid);
                    f = true;
                }
            }
        }
        int res = -1;
        for(int c1 = 2; res==-1; c1++){
            for(int i=0; i<R && res==-1; i++){
                for(int j=0; j<C && res==-1; j++){
                    if(grid[i][j] == c1){
                        if(extend(i, j, c1+1, R, C, grid)) res = c1-2;
                    }
                }
            }
        }
        return res;
    }
};
