class Solution {
    
    int dr[4]={-1,1,0,0};
    int dc[4]={0,0,-1,1};
    
    int R;
    int C;
    
    vector<vector<int>> _grid;
        
    int floodfill(int r,int c, int c1, int c2){
        if(r<0 || r>=R || c<0 || c>=C) return 0;
        if(_grid[r][c]!=c1) return 0;
        int ans=1;
        _grid[r][c]=c2;
        for(int d=0;d<4;d++)
            ans+= floodfill(r+dr[d],c+dc[d],c1,c2);
        return ans;
    }
    
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        _grid=grid;
        R=grid.size();
        C=grid[0].size();
        int m=0;
        for(int i=0;i<R;i++){
            for(int j=0;j<C;j++){
                m=max(m,floodfill(i,j,1,-1));
            }
        }
        return m;
    }
};
