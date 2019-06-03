/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
    vector<int> res;
    void postOrder(Node* root){
        if(!root)
            return;
        for(int i=0; i<root->children.size(); i++){
            postOrder(root->children[i]); 
        }
        res.push_back(root->val);
    }
public:
    vector<int> postorder(Node* root) {
        postOrder(root); 
        return res; 
    }
};
