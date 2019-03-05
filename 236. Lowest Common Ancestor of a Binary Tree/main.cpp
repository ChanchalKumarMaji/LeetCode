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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(!root)
            return NULL;
        if(root->val == p->val || root->val == q->val )
            return root;
        
        TreeNode *lCA_left = lowestCommonAncestor(root->left, p, q);
        TreeNode *lCA_right = lowestCommonAncestor(root->right, p, q);
        
        if(lCA_left && lCA_right)
            return root;
        
        if(lCA_left)
            return lCA_left;
        else
            return lCA_right;
        
    }
};
