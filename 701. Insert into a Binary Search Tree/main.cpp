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
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        TreeNode* newNode = new TreeNode(val);
        if(!root) return newNode;
        TreeNode* pos = root;
        while(1){
            if(pos->val > val){
                if(!pos->left){
                    pos->left = newNode;
                    break;
                }
                pos = pos->left;
            }
            else{
                if(!pos->right){
                    pos->right = newNode;
                    break;
                }
                pos = pos->right;
            }
        }
        return root;
    }
};
