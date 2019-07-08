class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int l=cost.size();
        vector<int> dp(l,0);
        dp[l-1]=cost[l-1];
        dp[l-2]=cost[l-2];
        for(int i=l-3;i>=0;i--){
            dp[i]=cost[i]+min(dp[i+1],dp[i+2]);
        }
        return min(dp[0],dp[1]);
    }
};
