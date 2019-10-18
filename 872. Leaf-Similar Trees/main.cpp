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
    void inOrder(TreeNode* root, vector<int>& res){
        if(!root) return;
        inOrder(root->left, res);
        if(!root->left && !root->right)
            res.push_back(root->val);
        inOrder(root->right, res);
    }
public:
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int> v1, v2;
        inOrder(root1, v1);
        inOrder(root2, v2);
        
        return v1 == v2; 
    }
};
