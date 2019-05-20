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
    int m = 0;
    int maxDepth(TreeNode* root){
        if(root == NULL)
            return 0;
        int lDepth = maxDepth(root->left);
        int rDepth = maxDepth(root->right);
        m = max(lDepth+rDepth, m);
        return 1 + max(lDepth, rDepth);
    }
public:
    int diameterOfBinaryTree(TreeNode* root) {
        //if(root == NULL)
        //    return 0;
        //return max(maxDepth(root->left) + maxDepth(root->right), max(diameterOfBinaryTree(root->left), diameterOfBinaryTree(root->right))); 
        maxDepth(root);
        return m;
    }
};
