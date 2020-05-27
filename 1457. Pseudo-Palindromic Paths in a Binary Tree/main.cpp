/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    vector<int> count;
    int res = 0;
    bool check(){
        int o = 0;
        for(int i=1; i<= 9; i++){
            if(count[i] % 2 == 1) o++;
        }
        return o <= 1;
    }
    void inOrder(TreeNode* root){
        if(!root) return;
        count[root->val]++;
        inOrder(root->left);
        inOrder(root->right);
        if(!root->left && !root->right && check())
            res++;
        count[root->val]--;
    }
public:
    int pseudoPalindromicPaths (TreeNode* root) {
        count.assign(10, 0);
        inOrder(root);
        return res;
    }
};
