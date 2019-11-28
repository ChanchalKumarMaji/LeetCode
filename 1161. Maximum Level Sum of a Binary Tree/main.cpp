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
    int maxLevelSum(TreeNode* root) {
        int sum, level = 0, res, max_sum = INT_MIN;
        queue<TreeNode*> q; q.push(root);
        while(!q.empty()){
            int nodeCount = q.size();
            sum = 0; level++;
            while(nodeCount--){
                TreeNode* node = q.front(); q.pop(); sum += node->val;
                if(node->left) q.push(node->left);
                if(node->right) q.push(node->right);
            }
            if(max_sum < sum){
                max_sum = sum;
                res = level;
            }
        }
        return res;
    }
};

