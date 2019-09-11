typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

// To store the graph
vector<vii> AdjList;

// To check whether vertex has been visited or not while performing dfs
vi dfs_num;

// To store quietness globally
vi check;

// ans and m store the person and minimum quietness value for each dfs
int ans = 0;
int m = 0;

// A simple function to perform dfs
void dfs(int u) {
    dfs_num[u] = 0;
    
    // Updating and storing the person relative to the given conditions
    if(check[u]<m){
        m = check[u];
        ans = u;
    }
    
    for (int j = 0; j < (int)AdjList[u].size(); j++) {
    ii v = AdjList[u][j];
    if (dfs_num[v.first] == 1)
    dfs(v.first);
} }

class Solution {
public:
    vector<int> loudAndRich(vector<vector<int>>& richer, vector<int>& quiet) {
        check = quiet;
        int n = quiet.size();
        
        // Creating the Graph
        AdjList.assign(n, vii());
        for(int i=0; i<richer.size(); i++){
            vector<int> vec = richer[i];
            AdjList[vec[1]].push_back(ii(vec[0], 0)); 
        }
        
        vi result; // To store the final result
        result.assign(n, 0);
        
        // Performing dfs on each node
        for(int i=0; i<n; i++){
            ans = i;
            m = quiet[i];
            dfs_num.assign(n, 1);
            dfs(i);
            result[i] = ans;
        }
        return result;
    }
};
