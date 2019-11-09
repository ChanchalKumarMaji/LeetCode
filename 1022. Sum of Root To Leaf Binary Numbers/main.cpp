/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
typedef pair<TreeNode*, int> ii;
class Solution {
public:
    int sumRootToLeaf(TreeNode* root) {
        if(!root) return 0;
        queue<ii> q; q.push(ii(root, root->val));
        int sum=0;
        while(!q.empty()){
            int nodeCount=q.size();
            while(nodeCount--){
                ii temp=q.front(); q.pop();
                TreeNode* node=temp.first;
                int res=temp.second;
                if(node->left) {
                    q.push(ii(node->left, res*2+node->left->val));
                }
                if(node->right){
                    q.push(ii(node->right, res*2+node->right->val));
                }
                if(!node->left && !node->right){
                    sum += res;
                }
            }
        }
        return sum;
    }
};
