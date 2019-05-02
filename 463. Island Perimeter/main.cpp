class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int res = 0; 
        int R = grid.size(), C = grid[0].size(); 
        for(int r = 0; r<R; r++)
            for(int c = 0; c<C; c++){
                if(grid[r][c] == 1){
                    if(r-1 == -1 || grid[r-1][c] == 0){
                        res++;
                    }
                    if(r+1 == R || grid[r+1][c] == 0){
                        res++;
                    }
                    if(c-1 == -1 || grid[r][c-1] == 0){
                        res++;
                    }
                    if(c+1 == C || grid[r][c+1] == 0){
                        res++; 
                    } 
                }
            }
        return res; 
    }
};
