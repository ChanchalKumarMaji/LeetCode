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
    vector<TreeNode*> nodes;
    
    void inOrder(TreeNode* root){
        if(!root) return;
        inOrder(root->left);
        nodes.push_back(root);
        inOrder(root->right);
    }
    
    TreeNode* sortedArrayToBST(int start, int end){
        if(start>=end) return NULL;
        int midIdx = (start+end)/2;
        TreeNode* root = nodes[midIdx];
        root->left = sortedArrayToBST(start, midIdx);
        root->right = sortedArrayToBST(midIdx+1, end);
        return root;
    }
public:
    TreeNode* balanceBST(TreeNode* root) {
        inOrder(root);
        return sortedArrayToBST(0, nodes.size());
    }
};
