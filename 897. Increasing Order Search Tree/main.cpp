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
    vector<TreeNode*> res;
    void inOrder(TreeNode* root){
        if(!root) return;
        inOrder(root->left);
        res.push_back(root);
        inOrder(root->right);
    }
public:
    TreeNode* increasingBST(TreeNode* root) {
        inOrder(root);
        root = res[0];
        root->left = NULL;
        root->right = NULL;
        TreeNode* node=root;
        for(int i=1; i<res.size(); i++){
            res[i]->left = NULL;
            res[i]->right = NULL;
            node->right = res[i];
            node = res[i];
        }
        return root;
    }
};
