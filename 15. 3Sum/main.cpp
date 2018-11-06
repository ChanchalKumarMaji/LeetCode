class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        if(nums.size()==0)
            return res;
        
        sort(nums.begin(),nums.end());
        
        int k,l,r,s;
        for(k=0;k<nums.size()-2;k++){
            if(nums[k]>0)
                break;
            if(k>0 and nums[k]==nums[k-1])
                continue;
            l=k+1;
            r=nums.size()-1;
            while(l<r){
                s=nums[k]+nums[l]+nums[r];
                if(s>0)
                    r--;
                else if (s<0)
                    l++;
                else{
                    res.push_back(vector<int>({nums[k],nums[l],nums[r]}));
                    while(l<r and nums[l]==nums[l+1])
                        l++;
                    while(l<r and nums[r]==nums[r-1])
                        r--;
                    l++;
                    r--;
                }
            }
        }
        return res;
    }
};
