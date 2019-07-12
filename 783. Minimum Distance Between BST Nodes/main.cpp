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
    int minDiffInBST(TreeNode* root) {
        inOrder(root);
        int ans=res[1]-res[0];
        for(int i=1; i<res.size(); i++){
            ans = min(ans, abs(res[i]-res[i-1]));
        }
        return ans;
    }
};
