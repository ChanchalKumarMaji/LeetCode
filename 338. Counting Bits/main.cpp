class Solution {
public:
    vector<int> countBits(int num) {
        
        vector<int> v(num+1,0);
        for(int i=1;i<=num;i++)
            v[i]=v[i & (i-1)]+1;
        
        return v;
        
    }
};
