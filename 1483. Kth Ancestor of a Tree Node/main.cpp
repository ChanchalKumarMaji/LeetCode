int p[100000][40]={{0}};
int a[100005];
class TreeAncestor {
public:
    TreeAncestor(int n, vector<int>& parent) {
        memset(p,0,sizeof(p));
        int i, x, y, j;
        for(i = 0;i < n;i++){
            x = i+1;
            y = parent[i]+1;
            a[i] = x;
            p[x][0] = y;
        }
        int lgn = (int)(log(n)/log(2))+1;
        for(j = 1;j<=lgn;j++){
            for(i = 0;i < n;i++){
                p[a[i]][j] = p[p[a[i]][j-1]][j-1];
            }
        }
    }
    
    int getKthAncestor(int node, int k) {
        int x, y, j;
        x = node+1;
        y = k;
        j = 0;
        while(y>0){
            if(y&1)
                x = p[x][j];
            y = y>>1;
            j++;
        }
        return x-1;
    }
};

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * TreeAncestor* obj = new TreeAncestor(n, parent);
 * int param_1 = obj->getKthAncestor(node,k);
 */
