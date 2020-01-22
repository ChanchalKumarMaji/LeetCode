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
    TreeNode* postOrder(TreeNode* root, int target){
        if(!root) return NULL;
        root->left = postOrder(root->left, target);
        root->right = postOrder(root->right, target);
        return (root->val == target && !root->left && !root->right) ? NULL : root;
    }
public:
    TreeNode* removeLeafNodes(TreeNode* root, int target) {
        return postOrder(root, target);
    }
};
