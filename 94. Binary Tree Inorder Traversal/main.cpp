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
    vector<int> inorderTraversal(TreeNode* root) {
        stack<TreeNode*> sta;
        vector<int> res;
        TreeNode* curr = root;
        while(curr || !sta.empty()){ 
            while(curr){
                sta.push(curr);
                curr = curr->left;
            }
            curr = sta.top(); sta.pop(); 
            res.push_back(curr->val); 
            curr = curr->right; 
        } 
        return res; 
    }
};
