/*
// Definition for a Node.
class Node {
public:
    int val = NULL;
    vector<Node*> children;

    Node() {}

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        vector<vector<int> > res;
        if(!root)
            return res; 
        queue<Node*> q; q.push(root); 
        while(!q.empty()){
            int nodeCount = q.size();
            vector<int> v;
            while(nodeCount--){
                Node* node = q.front(); q.pop(); 
                v.push_back(node->val); 
                for(auto e : node->children){
                    if(e)
                        q.push(e); 
                }
            }
            res.push_back(v); 
        }
        return res; 
    }
};
