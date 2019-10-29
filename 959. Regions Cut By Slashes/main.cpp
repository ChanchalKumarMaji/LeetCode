typedef vector<int> vi;
class Solution {
    vi p;
    int numSets = 0, N = 0;
public:
    int findSet(int i){
        return (p[i] == i) ? i : (p[i] = findSet(p[i]));
    }
    bool isSameSet(int i, int j){
        return findSet(i) == findSet(j);
    }
    void unionSet(int i, int j){
        int x = findSet(i), y = findSet(j);
        if(!isSameSet(x, y)){
            numSets--;
            p[x] = y;
        }
    }
    int val(int i, int j, int k){
        return (N*i + j)*4 + k;
    }
    
    int regionsBySlashes(vector<string>& grid) {
        N = grid.size();
        p.assign(N*N*4, 0); for(int i=0; i<N*N*4; i++) p[i] = i;
        numSets = N*N*4;
        for(int i=0; i<N; i++){
            for(int j = 0; j<N; j++){
                if(j+1 < N) unionSet(val(i, j, 3), val(i, j+1, 1));
                if(i+1 < N) unionSet(val(i, j, 2), val(i+1, j, 0));
                if(grid[i][j] == ' '){
                    unionSet(val(i, j, 0), val(i, j, 1));
                    unionSet(val(i, j, 1), val(i, j, 2));
                    unionSet(val(i, j, 2), val(i, j, 3));
                }
                else if(grid[i][j] == '/'){
                    unionSet(val(i, j, 0), val(i, j, 1));
                    unionSet(val(i, j, 2), val(i, j, 3));
                }
                else if(grid[i][j] == '\\'){
                    unionSet(val(i, j, 0), val(i, j, 3));
                    unionSet(val(i, j, 1), val(i, j, 2));
                }
            }
        }
        
        return numSets;
    }
};
