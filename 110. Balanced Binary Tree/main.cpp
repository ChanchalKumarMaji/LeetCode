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
    int height(TreeNode* root){
        if(!root)
            return 0;
        return 1 + max(height(root->left), height(root->right)); 
    }
public:
    bool isBalanced(TreeNode* root) {
        if(!root)
            return true;
        
        int hl = height(root->left);
        int hr = height(root->right);
        
        return abs(hl-hr)<=1 && isBalanced(root->left) && isBalanced(root->right);  
    }
};
