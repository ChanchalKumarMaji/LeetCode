class Solution {
public:
    vector<int> pathInZigZagTree(int label) {
        vector<int> res;
        int level = 0;
        while(1<<level <= label) level++;
        for(; level>0; level--){
            int parent = (((1<<level) - 1) + (1<<(level-1)) - label) / 2;
            res.push_back(label);
            label = parent;
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
