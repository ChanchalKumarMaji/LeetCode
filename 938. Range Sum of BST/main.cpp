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
    int res=0, l, r;
    void inOrder(TreeNode* root){
        if(!root) return;
        inOrder(root->left);
        if(root->val>=l && root->val<=r) res += root->val;
        inOrder(root->right);
    }
public:
    int rangeSumBST(TreeNode* root, int L, int R) {
        l = L; r = R;
        inOrder(root);
        return res;
    }
};
