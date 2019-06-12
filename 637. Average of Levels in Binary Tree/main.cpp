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
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> res;
        
        queue<TreeNode*> q;
        q.push(root); 
        
        while(!q.empty()){ 
            int nodeCount=q.size();
            int k=nodeCount; 
            double sum=0; 
            while(k--){
                TreeNode* node=q.front();
                q.pop();
                sum += node->val;
                if(node->left!=NULL)
                    q.push(node->left);
                if(node->right!=NULL)
                    q.push(node->right);
            }
            res.push_back(sum/nodeCount);  
        }
        
        return res;
    }
};
