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
    int findBottomLeftValue(TreeNode* root) {
        queue<TreeNode*> q;
        int res;
        q.push(root);
        while(!q.empty()){
            int nodeCount = q.size();
            res = q.front()->val; 
            for(int i=0; i<nodeCount; i++){
                TreeNode* node = q.front();
                q.pop(); 
                if(node->left)
                    q.push(node->left);
                if(node->right)
                    q.push(node->right); 
            }
        }
        return res;
    }
};
