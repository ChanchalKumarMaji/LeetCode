/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> res; 
        if(!root)
            return res;
        int count = 1;
        queue<TreeNode*> q; q.push(root); 
        while(!q.empty()){
            int nodeCount = q.size();
            vector<int> v;
            while(nodeCount--){
                TreeNode* node = q.front(); q.pop();
                if(node->left)
                    q.push(node->left);
                if(node->right)
                    q.push(node->right); 
                v.push_back(node->val);
            }
            if(count%2==0)
                reverse(v.begin(), v.end()); 
            count++; 
            res.push_back(v); 
        }
        return res;
    }
};
