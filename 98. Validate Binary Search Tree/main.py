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
    vector<int> v;
    void inOrder(TreeNode* node){
        if(node==NULL) 
            return;
        inOrder(node->left);
        v.push_back(node->val);
        inOrder(node->right); 
    }
    bool isValidBST(TreeNode* root) {
        inOrder(root);
        for(int i=1;i<v.size();i++){
            
            if(v[i]<=v[i-1])
                return false;
        }
        return true;
    }
};
