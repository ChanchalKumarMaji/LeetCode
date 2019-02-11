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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> v;
        if(!root)
            return v;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            int nodeCount = q.size();
            nodeCount--;
            while(nodeCount--){
                TreeNode* node = q.front();
                q.pop();
                if(node->left)
                    q.push(node->left);
                if(node->right)
                    q.push(node->right);
            }
            TreeNode* node = q.front();
            q.pop();
            v.push_back(node->val); 
            if(node->left)
                q.push(node->left);
            if(node->right)
                q.push(node->right); 
        }
        return v; 
    }
};
