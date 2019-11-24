typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

class Solution {
    vector<vii> AdjList;
    vi dfs_num;
    vi dfs_low;
    vi dfs_parent;
    int dfsNumberCounter = 1;
    vector<vi> res;
public:
    void articulationPointAndBridge(int u){
        dfs_low[u] = dfs_num[u] = dfsNumberCounter++;
        for(int j=0; j<AdjList[u].size(); j++){
            ii v = AdjList[u][j];
            if(dfs_num[v.first] == 0){
                dfs_parent[v.first] = u;
                articulationPointAndBridge(v.first);
                if(dfs_low[v.first] > dfs_num[u])
                    res.push_back(vi({u, v.first}));
                dfs_low[u] = min(dfs_low[u], dfs_low[v.first]);
            }
            else if(v.first != dfs_parent[u])
                dfs_low[u] = min(dfs_low[u], dfs_num[v.first]);
        }
    }
    
    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
        AdjList.assign(n, vii());
        for(auto connection : connections){
            int u = connection[0], v = connection[1];
            AdjList[u].push_back(ii(v, 1));
            AdjList[v].push_back(ii(u, 1));
        }
        dfs_num.assign(n, 0); dfs_low.assign(n, 0); dfs_parent.assign(n, 0);
        for(int i=0; i<n; i++){
            if(dfs_num[i] == 0){
                articulationPointAndBridge(i);
            }
        }
        //for(int i=0; i<n; i++) cout<<dfs_num[i]<<" ";
        //cout<<endl;
        //for(int i=0; i<n; i++) cout<<dfs_low[i]<<" ";
        //cout<<endl;
        
        return res;
    }
};
