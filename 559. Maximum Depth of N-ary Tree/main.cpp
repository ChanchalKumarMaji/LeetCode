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
public:
    int maxDepth(Node* root) {
        if(!root)
            return 0;
        int m = 0;
        for(int i=0; i<root->children.size(); i++){
            m = max(m, maxDepth(root->children[i]));
        }
        return 1+m;  
    }
};
