typedef pair<int, int> ii;
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        queue<ii> q;
        int R = grid.size(), C = grid[0].size(), ones = 0, res = 0;
        int dr[] = {1, 0, -1, 0};
        int dc[] = {0, 1, 0, -1};
        for(int i=0; i<R; i++){
            for(int j=0; j<C; j++){
                if(grid[i][j] == 2) q.push({i, j});
                if(grid[i][j] == 1) ones++;
            }
        }
        int dist[R][C]; for(int i=0; i<R; i++) for(int j=0; j<C; j++) dist[i][j] = 0;
        while(!q.empty()){
            ii u = q.front(); q.pop(); int r = u.first, c = u.second;
            for(int d=0; d<4; d++){
                int x = r+dr[d], y = c+dc[d];
                if(x<0 || x>=R || y<0 || y>=C || grid[x][y]==0 || grid[x][y]==2) continue;
                dist[x][y] = dist[r][c] + 1;
                grid[x][y] = 2;
                res = max(res, dist[x][y]);
                q.push({x, y}); ones--;
            }
        }
        return ones==0 ? res : -1;
    }
};
