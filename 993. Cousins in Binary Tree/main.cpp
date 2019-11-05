/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
typedef pair<TreeNode*, TreeNode*> TT;
class Solution {
public:
    bool isCousins(TreeNode* root, int x, int y) {
        queue<TT> q;
        if(root->left){
            q.push(TT(root->left, root));
        }
        if(root->right){
            q.push(TT(root->right, root));
        }
        while(!q.empty()){
            int nodeCount = q.size();
            int f1=0, f2=0;
            TreeNode* p1=NULL;
            TreeNode* p2=NULL;
            while(nodeCount--){
                TT node = q.front(); q.pop();
                TreeNode* temp = node.first;
                if(temp->val == x){
                    f1 = 1;
                    p1 = node.second;
                }
                if(temp->val == y){
                    f2 = 1;
                    p2 = node.second;
                }
                if(temp->left){
                    q.push(TT(temp->left, temp));
                }
                if(temp->right){
                    q.push(TT(temp->right, temp));
                }
            }
            if(f1==1 && f2==1 && p1 && p2 && p1 != p2){
                return true;
            }
        }
        return false;
    }
};
