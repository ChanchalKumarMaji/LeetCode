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
    bool res = true;
    int val;
    void inOrder(TreeNode* root){
        if(!root) return;
        inOrder(root->left);
        if(root->val != val) res=false;
        inOrder(root->right);
    }
public:
    bool isUnivalTree(TreeNode* root) {
        val = root->val;
        inOrder(root);
        return res;
    }
};
