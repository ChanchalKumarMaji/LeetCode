/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> findMode(TreeNode* root) {
        vector<int> res;
        map<int,int> d; 
        if(root==NULL) 
            return res;
        queue<TreeNode*> q;
        q.push(root); 
        
        while(!q.empty()){
            int nodeCount=q.size();
            while(nodeCount--){
                TreeNode* node=q.front();
                q.pop();
                d[node->val]+=1; 
                if(node->left!=NULL)
                    q.push(node->left);
                if(node->right!=NULL)
                    q.push(node->right);
            }
        }
        map<int,int>::iterator itr;
        int max_f=0;
        for(itr=d.begin();itr!=d.end();itr++){
            max_f=max(max_f,itr->second);
        }
        for(itr=d.begin();itr!=d.end();itr++){
            if(itr->second == max_f)
                res.push_back(itr->first); 
        }
        return res;
    }
};
