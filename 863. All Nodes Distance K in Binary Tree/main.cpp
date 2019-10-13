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
    
    vector<int> res;
    
void printkdistanceNodeDown(TreeNode *root, int K)
{
    
    if (root == NULL || K < 0)  return;
 
    
    if (K==0)
    {
        res.push_back(root->val); 
        return;
    }
 
    printkdistanceNodeDown(root->left, K-1);
    printkdistanceNodeDown(root->right, K-1);
}

int printkdistanceNode(TreeNode* root, TreeNode* target , int K)
{
    
    if (root == NULL) return -1;
 
   
    if (root == target)
    {
        printkdistanceNodeDown(root, K);
        return 0;
    }
 
    
    int dl = printkdistanceNode(root->left, target, K);
 
   
    if (dl != -1)
    {
         
         if (dl + 1 == K)
            res.push_back(root->val);
 
       
         else
            printkdistanceNodeDown(root->right, K-dl-2);
 
         return 1 + dl;
    }
 
    int dr = printkdistanceNode(root->right, target, K);
    if (dr != -1)
    {
         if (dr + 1 == K)
            res.push_back(root->val);
         else
            printkdistanceNodeDown(root->left, K-dr-2);
         return 1 + dr;
    }
 
    return -1;
}
public:
    vector<int> distanceK(TreeNode* root, TreeNode* target, int K) {
        printkdistanceNode(root, target, K);
        return res;
    }
};
