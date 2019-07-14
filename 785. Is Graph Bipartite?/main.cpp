class Solution {
    
    vector<vector<int>> AdjList;
    int V;
    vector<int> dfs_num;
    
    bool is_bipartite_for_connected_components(int s){
        queue<int> q; q.push(s);
        map<int,int> dist; dist[s]=0; dfs_num[s]=1;
        //bool isBipartite=true;
        
        while(!q.empty()){
            int u=q.front(); q.pop();
            for(int j=0;j<AdjList[u].size();j++){
                int v=AdjList[u][j];
                
                if(!dist.count(v)){
                    dist[v]=1-dist[u]; dfs_num[v]=1;
                    q.push(v);
                }
                else if(dist[v]==dist[u])
                    return false;
            }
        }    
        return true;
    }
    
    
public:
    bool isBipartite(vector<vector<int>>& graph) {
        AdjList=graph; 
        V=graph.size();
        dfs_num.assign(V,-1);
        for(int i=0;i<V;i++){
            if(dfs_num[i]==-1){
                if(is_bipartite_for_connected_components(i)==false)
                    return false;
            }
        }
        return true; 
    }
};
