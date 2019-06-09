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
        stack<Tii> s; s.push(Tii(root, ii(root->val, root->val)));
        int res = 0;
        while(!s.empty()){
            int nodeCount = s.size();
            while(nodeCount--){
                Tii temp = s.top(); s.pop();
                TreeNode* node = temp.first;
                ii p = temp.second;
                if(node->left){
                    s.push(Tii(node->left, ii(max(p.first, node->left->val), min(p.second, node->left->val))));
                }
                if(node->right){
                    s.push(Tii(node->right, ii(max(p.first, node->right->val), min(p.second, node->right->val))));
                }
                if(!node->left && !node->right){
                    res = max(res, abs(p.first-p.second));
                }
            }
        }
        return res;
    }
};
