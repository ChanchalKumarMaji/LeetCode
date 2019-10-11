typedef pair<int, int> ii;
class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        if(grid[0][0] == 1) return -1;
        queue<ii> q; q.push(ii(0, 0));
        int dr[] = {1, -1, 0, 0, 1, 1, -1, -1};
        int dc[] = {0, 0, 1, -1, 1, -1, 1, -1};
        int R = grid.size(), C = grid[0].size();
        int dist[R][C]; 
        for(int i=0; i<R; i++) for(int j=0; j<C; j++) dist[i][j] = 0;
        dist[0][0] = 1;
        while(!q.empty()){
            ii u = q.front(); q.pop(); int r = u.first, c = u.second;
            for(int d=0; d<8; d++){
                int x = r+dr[d], y = c+dc[d];
                if(x<0 || x>=R || y<0 || y>=C || grid[x][y] == 1) continue;
                if(dist[x][y] == 0){
                    dist[x][y] = dist[r][c] + 1;
                    q.push(ii(x, y));
                }
            }
        }
        if(dist[R-1][C-1] == 0) return -1;
        else return dist[R-1][C-1];
    }
};
