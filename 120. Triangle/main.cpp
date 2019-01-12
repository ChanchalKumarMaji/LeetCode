class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int length=triangle.size();
        vector<int> dp(triangle.back());
        int i,j;
        //for(i=0;i<length;i++)
        //    dp[i]=triangle[length-1][i];
        for(i=length-1-1;i>=0;i--){
            for(j=0;j<=i;j++){
                dp[j]=triangle[i][j] + min(dp[j],dp[j+1]);
            }
        }
        return dp[0];
    }
};
