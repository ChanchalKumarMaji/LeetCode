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
    vector<int> res;
    void inOrder(TreeNode* root){
        if(!root) return;
        inOrder(root->left);
        res.push_back(root->val);
        inOrder(root->right);
    }
public:
    vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
        inOrder(root1);
        inOrder(root2);
        sort(res.begin(), res.end());
        return res;
    }
};
