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
    vector<int> largestValues(TreeNode* root) {
        vector<int> res;
        if(!root)
            return res;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            int nodeCount = q.size();
            int k = -2147483648;
            for(int i=0; i<nodeCount; i++){
                TreeNode* node = q.front();
                k = max(k, node->val);
                if(node->left)
                    q.push(node->left);
                if(node->right)
                    q.push(node->right);   
                q.pop();
            }
            res.push_back(k); 
        }
        return res;
    }
};
