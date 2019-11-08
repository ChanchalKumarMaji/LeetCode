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
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        TreeNode* root = new TreeNode(preorder[0]);
        for(int i=1; i<preorder.size(); i++){
            TreeNode* newNode = new TreeNode(preorder[i]);
            TreeNode* pos = root;
            while(1){
                if(pos->val > preorder[i]){
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
        }        
    return root;
    }
};
