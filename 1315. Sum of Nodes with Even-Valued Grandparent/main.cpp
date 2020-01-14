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
typedef pair<TreeNode*, ii> p;

class Solution {
public:
    int sumEvenGrandparent(TreeNode* root) {
        int res = 0;
        queue<p> q; q.push(p(root, ii(-1, -1)));
        while(!q.empty()){
            int nodeCount = q.size();
            while(nodeCount--){
                p temp = q.front(); q.pop();
                TreeNode* node = temp.first;
                int a = temp.second.first, b = temp.second.second;
                if(node->left) q.push(p(node->left, ii(node->val, a)));
                if(node->right) q.push(p(node->right, ii(node->val, a)));
                if(b % 2 == 0) res += node->val;
            }
        }
        return res;
    }
};
