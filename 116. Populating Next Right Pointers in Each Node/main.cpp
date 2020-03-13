/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
class Solution {
public:
    void connect(TreeLinkNode *root) {
        if(!root)
            return; 
        queue<TreeLinkNode*> q;
        q.push(root);
        while(!q.empty()){
            int nodeCount = q.size()-1;
            TreeLinkNode* pre = q.front();
            q.pop();
            if(pre->left)
                q.push(pre->left);
            if(pre->right)
                q.push(pre->right); 
            while(nodeCount--){
                TreeLinkNode* node = q.front();
                q.pop();
                if(node->left)
                    q.push(node->left);
                if(node->right)
                    q.push(node->right); 
                pre->next = node;
                pre = node;
            }
            
        }
    }
};
 
