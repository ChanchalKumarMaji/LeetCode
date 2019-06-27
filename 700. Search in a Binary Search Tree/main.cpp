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
    TreeNode* searchBST(TreeNode* root, int val) {
        while(true){
            if(!root)
                return NULL;
            if(root->val == val){
                return root;
            }
            else if(root->val < val){
                root = root->right;
            }
            else if(root->val > val){
                root = root->left; 
            }
        }    
    }
};
