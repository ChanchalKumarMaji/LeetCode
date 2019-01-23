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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<TreeNode*> sta;
        TreeNode* curr = root;
        while(curr || !sta.empty()){
            while(curr){
                sta.push(curr);
                res.push_back(curr->val); 
                curr = curr->left;
            }
            curr = sta.top(); sta.pop();
            
            curr = curr->right; 
        }
        return res;
    }
};
