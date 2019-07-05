class Solution {
    vector<vector<int>> grid;
    int R, C;
    int dr[4] = {0, 0, 1, -1};
    int dc[4] = {1, -1, 0, 0}; 
    void floodfill(int r, int c, int c1, int c2){
        if(r<0 || r>=R || c<0 || c>=C) return;
        if(grid[r][c] != c1) return;
        grid[r][c] = c2;
        for(int d=0; d<4; d++){
            floodfill(r+dr[d], c+dc[d], c1, c2);
        }    
    }
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        R = image.size();
        C = image[0].size();
        grid = image; 
        if(image[sr][sc] == newColor)
            return image; 
        floodfill(sr, sc, image[sr][sc], newColor);
        return grid;
    }
};
