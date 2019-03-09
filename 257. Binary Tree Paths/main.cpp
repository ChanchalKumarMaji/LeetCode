/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

typedef pair<TreeNode*, string> p;

class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> res; 
        string s;
        if(!root)
            return res;
        queue<p> q;    
        q.push(p(root, "")); 
        while(!q.empty()){
            TreeNode *cur,*l,*r; 
            cur = (q.front()).first;
            s = (q.front()).second; 
            q.pop();
            
            if(s!="")
                s = s + "->" + to_string(cur->val);  
            else
                s = to_string(cur->val);
            
            if(!cur->left && !cur->right){ 
                res.push_back(s);  
            }
            else if(!cur->left && cur->right){
                r = cur->right;
                q.push(p(r, s));
            }
            else if(cur->left && !cur->right){
                l = cur->left;
                q.push(p(l, s));
            }
            else{
                r = cur->right;
                q.push(p(r, s));
                l = cur->left;
                q.push(p(l, s)); 
            }   
        }
        return res;
    }
};
