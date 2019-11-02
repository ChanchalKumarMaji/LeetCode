/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
typedef pair<TreeNode*, int> Ti;
class Solution {
public:
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        map<int, vector<int>> d;
        queue<Ti> q; q.push(Ti(root, 0));
        while(!q.empty()){
            int nodeCount = q.size();
            map<int, set<int>> t;
            while(nodeCount--){
                Ti temp = q.front(); q.pop();
                TreeNode* node = temp.first;
                int p = temp.second;
                t[p].insert(node->val);
                if(node->left){
                    q.push(Ti(node->left, p-1));
                }
                if(node->right){
                    q.push(Ti(node->right, p+1));
                }
            }
            for(auto it=t.begin(); it!=t.end(); it++){
                for(auto e:it->second)
                    d[it->first].push_back(e);
            }
        }
        vector<vector<int>> res;
        for(auto it=d.begin(); it!=d.end(); it++){
            res.push_back(it->second);
        }
        return res;
    }
};
