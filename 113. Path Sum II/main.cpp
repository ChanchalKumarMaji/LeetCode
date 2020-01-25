/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

typedef vector<int> vi;
typedef pair<TreeNode*, vi> p;

class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vi> res;
        if(!root)
            return res;
        queue<p> q; 
        vi temp;
        //v.push_back(root->val);
        q.push(p(root, temp)); 
        while(!q.empty()){
            TreeNode *cur,*l,*r;
            vi vec;
            
            cur = (q.front()).first;
            vec = (q.front()).second;
            q.pop();
            
            if(!cur->left && !cur->right){
                vec.push_back(cur->val); 
                int s=0;
                for(int i=0; i<vec.size(); i++){
                    s += vec[i];
                }
                if(s == sum)
                    res.push_back(vec); 
            }
            else if(!cur->left && cur->right){
                r = cur->right;
                vec.push_back(cur->val);  
                q.push(p(r, vec));
            }
            else if(cur->left && !cur->right){
                l = cur->left;
                vec.push_back(cur->val); 
                q.push(p(l, vec));
            }
            else{
                vi vec1 = vec, vec2 = vec;
                r = cur->right;
                vec1.push_back(cur->val); 
                q.push(p(r, vec1));
                l = cur->left;
                vec2.push_back(cur->val); 
                q.push(p(l, vec2)); 
            }   
        }
        
        return res; 
    }
};
