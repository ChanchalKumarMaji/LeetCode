class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        vector<int> dp(nums.size()+1,0);
        for(int i=0;i<nums.size();i++){
            dp[i+1]=nums[i]+dp[i];
        }
        int c=0;
        for(int i=0;i<dp.size()-1;i++){
            for(int j=i+1;j<dp.size();j++){
                if(dp[j]-dp[i]==k)
                    c++;
            }
        }
        return c;
    }
};
