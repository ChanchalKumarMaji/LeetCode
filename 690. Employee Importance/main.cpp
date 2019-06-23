/*
// Employee info
class Employee {
public:
    // It's the unique ID of each node.
    // unique id of this employee
    int id;
    // the importance value of this employee
    int importance;
    // the id of direct subordinates
    vector<int> subordinates;
};
*/

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

class Solution {
    map<int, int> dfs_num;
    map<int, vi> AdjList;
    map<int, int> imp;
    int res = 0;
    void dfs(int u){
        dfs_num[u] = 1;
        res += imp[u]; 
        for(int j=0; j<AdjList[u].size(); j++){
            int v = AdjList[u][j];
            if(dfs_num[v] == 0)
                dfs(v);  
        } 
    }
    
public:
    int getImportance(vector<Employee*> employees, int id) {
        for(int i=0; i<employees.size(); i++){
            Employee* p = employees[i];
            int _id = p->id;
            int _importance = p->importance; 
            vi _subordinates = p->subordinates; 
            imp[_id] = _importance; 
            AdjList[_id] = _subordinates;
            dfs_num[_id] = 0;
        }
        dfs(id);
        return res; 
    }
};
