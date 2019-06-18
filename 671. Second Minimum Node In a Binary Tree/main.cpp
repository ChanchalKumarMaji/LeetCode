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
    set<int> s;
    void inOrder(TreeNode* root){
        if(root == NULL)
            return;
        inOrder(root->left);
        s.insert(root->val); 
        inOrder(root->right);
    }
public:
    int findSecondMinimumValue(TreeNode* root) {
        if(!root)
            return -1;
        inOrder(root);
        if(s.size()<=1)
            return -1;
        else{
            set<int> :: iterator itr = s.begin();
            itr++;
            return *itr; 
        }
    } 
};
