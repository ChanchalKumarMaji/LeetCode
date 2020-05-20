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
typedef pair<TreeNode*, int> p;
class Solution {
public:
    int goodNodes(TreeNode* root) {
        int res = 0;
        queue<p> q; q.push(p(root, -100000));
        while(!q.empty()){
            int nodeCount = q.size();
            while(nodeCount--){
                p temp = q.front(); q.pop();
                TreeNode* node = temp.first;
                if(node->val >= temp.second) res++;
                if(node->left) q.push(p(node->left, max(temp.second, node->val)));
                if(node->right) q.push(p(node->right, max(temp.second, node->val)));
            }
        }
        return res;
    }
};
