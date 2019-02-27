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
    int kthSmallest(TreeNode* root, int k) {
        stack<TreeNode*> sta;
        TreeNode* curr=root;
        int t = 0;
        while(curr || !sta.empty()){
            while(curr){
                sta.push(curr);
                curr = curr->left;
            }
            curr = sta.top(); sta.pop();
            t++;
            if(t == k)
                return curr->val; 
            curr = curr->right; 
        }
    }
};
