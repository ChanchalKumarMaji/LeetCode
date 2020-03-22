class Solution {
public:
    int numSquares(int n) {
        vector<int> dp(n+1, 100000);
        dp[0] = 0;
        for(int i=1; i<n+1; i++){
            for(int j=1; i-j*j>=0; j++){
                dp[i] = min(dp[i], dp[i-j*j]+1);
            }
        }
        return dp[n];
    }
};
