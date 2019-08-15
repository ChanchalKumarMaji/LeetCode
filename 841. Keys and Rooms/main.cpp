typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;



class Solution {
    vi dfs_num;
    vector<vii> AdjList;
    int numCC=0;
    void dfs(int u) {
        dfs_num[u] = 1;
        for (int j = 0; j < (int)AdjList[u].size(); j++) {
            ii v = AdjList[u][j];
            if (dfs_num[v.first] == -1)
                dfs(v.first);
        } 
    }
    
    
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int V = rooms.size();
        AdjList.assign(V,vii());
        for(int i=0;i<rooms.size();i++){
            for(int j=0;j<rooms[i].size();j++){
                AdjList[i].push_back(ii(rooms[i][j], 0)); 
            }
        }
        
        dfs_num.assign(V, -1);
        
        for (int i = 0; i < V ; i++)
            if (dfs_num[i] == -1){
                ++numCC;
                dfs(i);
            }
        
        cout<<numCC<<endl; 
        
        if(numCC==1)
            return true;
        return false;
    }
};
