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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<TreeNode*> sta;
        TreeNode* curr = root;
        while(curr || !sta.empty()){
            while(curr){
                sta.push(curr);
                res.push_back(curr->val);   
                curr = curr->right;
            }
            curr = sta.top(); sta.pop();
            
            curr = curr->left; 
        }
        reverse(res.begin(), res.end()); 
        return res;
    }
};
