class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
       
        if(nums.size()==0)
            return 0;
        
        int m=nums[0];
        for(int k:nums){
            m=max(m,k);
        }
        
        vector<int> v(m+1,0);
        for(int k:nums){
            v[k]=v[k]+k;
        }
        
        vector<int> dp(m+1,0);
        
        dp[0]=v[0];
        if(m==0)
            return dp[0];
        
        dp[1]=max(v[0],v[1]);
        for(int i=2;i<m+1;i++){
            dp[i]=max(dp[i-1],dp[i-2]+v[i]);
        }
        
        return dp[m];
        
    }
};
