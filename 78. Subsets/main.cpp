class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> sub;
        int n=nums.size();
        for(int i=0;i<pow(2,n);i++){
            int k=i;
            vector<int> p;
            for(int j=0;j<n;j++){
                if(k & 1)
                    p.push_back(nums[j]);
                k>>=1;
            }
            sub.push_back(p);
        }
            
        return sub;
        
    }
};
