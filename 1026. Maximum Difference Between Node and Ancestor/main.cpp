/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
typedef pair<int, int> ii;
typedef pair<TreeNode*, ii> Tii;
class Solution {
public:
    int maxAncestorDiff(TreeNode* root) {
        queue<Tii> q; q.push(Tii(root, ii(root->val, root->val)));
        int res = 0;
        while(!q.empty()){
            int nodeCount = q.size();
            while(nodeCount--){
                Tii temp = q.front(); q.pop();
                TreeNode* node = temp.first;
                ii p = temp.second;
                if(node->left){
                    q.push(Tii(node->left, ii(max(p.first, node->left->val), min(p.second, node->left->val))));
                }
                if(node->right){
                    q.push(Tii(node->right, ii(max(p.first, node->right->val), min(p.second, node->right->val))));
                }
                if(!node->left && !node->right){
                    res = max(res, abs(p.first-p.second));
                }
            }
        }
        return res;
    }
};
