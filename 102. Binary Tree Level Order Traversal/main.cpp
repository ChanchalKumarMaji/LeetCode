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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if(root==NULL) 
            return res;
        queue<TreeNode*> q;
        q.push(root); 
        
        while(!q.empty()){
            int nodeCount=q.size();
            vector<int> v;
            while(nodeCount--){
                TreeNode* node=q.front();
                q.pop();
                v.push_back(node->val);
                if(node->left!=NULL)
                    q.push(node->left);
                if(node->right!=NULL)
                    q.push(node->right);
            }
            res.push_back(v); 
        }
        
        return res;
    }
};
