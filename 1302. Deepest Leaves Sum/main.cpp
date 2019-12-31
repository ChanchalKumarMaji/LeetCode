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
    int deepestLeavesSum(TreeNode* root) {
        map<int, int> d; 
        int depth = 0;
        queue<TreeNode*> q; q.push(root);
        while(!q.empty()){
            int sum = 0;
            depth++;
            int nodeCount = q.size();
            while(nodeCount--){
                TreeNode* node = q.front(); q.pop();
                if(node->left) q.push(node->left);
                if(node->right) q.push(node->right);
                if(!node->left && !node->right) sum += node->val;
            }
            d[depth] = sum;
        }
        
        return d[depth];
    }
};
