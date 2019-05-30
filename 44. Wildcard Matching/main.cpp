class Solution {
public:
    bool isMatch(string s, string p) {
        int m=s.length(), n=p.length();
        int dp[m+1][n+1];
        memset(dp, 0, sizeof dp);
        dp[0][0]=1;
        for(int j=1; j<n+1; j++){
            if(p[j-1]=='*') dp[0][j]=dp[0][j-1];
        }
        for(int i=1; i<m+1; i++){
            for(int j=1; j<n+1; j++){
                if(s[i-1]==p[j-1] || p[j-1]=='?') dp[i][j]=dp[i-1][j-1];
                else if(p[j-1]=='*') dp[i][j]=dp[i-1][j] | dp[i][j-1];
            }
        }
        return dp[m][n]==1;
    }
};
