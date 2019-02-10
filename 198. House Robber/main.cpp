class Solution {
public:
    int rob(vector<int>& nums) {
        //vector<int> dp(nums.size(),0);
        int a,b,c;
        if(nums.size()==0)
            return 0;
        
        //dp[0]=nums[0];
        a=nums[0];
        
        if(nums.size()==1)
            return a;
        
        //dp[1]=max(nums[0],nums[1]);
        b=max(nums[0],nums[1]);
        
        for(int i=2;i<nums.size();i++){
            c=max(b,a+nums[i]);
            a=b;
            b=c;
        }
        
        return b;
    }
};
