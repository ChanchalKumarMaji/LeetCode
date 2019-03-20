class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int length=nums.size();
        if(length==0)
            return 0;
        int dp[length];
        int i,j;
        for(i=0;i<length;i++){
            dp[i]=1;
        }
        for(i=1;i<length;i++){
            for(j=0;j<i;j++){
                if(nums[j]<nums[i])
                    dp[i]=max(dp[j]+1,dp[i]);
            }
        }
        int m=dp[0];
        for(i=0;i<length;i++){
            if(m<dp[i])
                m=dp[i];
        }
        
        return m;
        
    }
};
