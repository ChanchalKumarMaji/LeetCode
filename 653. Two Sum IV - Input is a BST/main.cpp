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
    map<int,int> m;
    void inOrder(TreeNode* root){
        if(root==NULL)
            return;
        inOrder(root->left);
        m[root->val]=1; 
        #cout<<root->val<<" ";
        inOrder(root->right);
    }
    bool findTarget(TreeNode* root, int k) {
        inOrder(root);
        map<int,int>::iterator itr;
        for(itr=m.begin();itr!=m.end();itr++){
            #cout<<itr->first<<" "<<itr->second<<endl;
            #cout<<itr->first<<endl;
            int p=itr->first;
            if(m.count(k-p)>0 and k-p!=p)
                return true;
        }
        return false;
    }
};
