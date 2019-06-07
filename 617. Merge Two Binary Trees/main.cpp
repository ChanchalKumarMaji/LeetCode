/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

typedef pair<TreeNode*, TreeNode*> p;
stack<p> s;

class Solution {
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if(!t1)
            return t2;
        if(!t2)
            return t1;
        
        s.push(p(t1,t2));
        
        while(!s.empty()){
            p nodes = s.top();
            s.pop(); 
            TreeNode* node1 = nodes.first;
            TreeNode* node2 = nodes.second;
            
            node1->val = node1->val + node2->val;
            
            if(!node1->left){
                node1->left = node2->left;
            }
            else if(node2->left){
                s.push(p(node1->left, node2->left));
            }
            
            if(!node1->right){
                node1->right = node2->right;
            }
            else if(node2->right){ 
                s.push(p(node1->right, node2->right));
            }
            
        }
        
        return t1;
        
    }
};
