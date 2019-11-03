/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
typedef pair<TreeNode*, string> Ts;
class Solution {   
    string reverse(string s){
        string rev="";
        for(int i=s.length()-1; i>=0; i--) rev += s[i];
        return rev;
    }
public:
    string smallestFromLeaf(TreeNode* root) {
        string s="";
        s += (char)(root->val+97);
        //stringstream ss;
        //ss << (char)(root->val+97);
        //ss >> s;
        queue<Ts> q; q.push(Ts(root, s));
        vector<string> res;
        while(!q.empty()){
            int nodeCount = q.size();
            while(nodeCount--){
                Ts temp = q.front(); q.pop();
                TreeNode* node = temp.first;
                s = temp.second;
                if(node->left){
                    q.push(Ts(node->left, s+(char)(node->left->val+97)));
                }
                if(node->right){
                    q.push(Ts(node->right, s+(char)(node->right->val+97)));
                }
                if(!node->left && !node->right){
                    res.push_back(reverse(s));
                }
            }
        }
        sort(res.begin(), res.end());
        return res[0];
    }
};
