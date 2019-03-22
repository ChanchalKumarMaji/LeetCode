class NumMatrix {
public:
    vector<vector<int>> dp;
    NumMatrix(vector<vector<int>> matrix) {
        for(int i=0;i<matrix.size();i++){
            vector<int> v;
            v.push_back(0);
            for(int j=0;j<matrix[i].size();j++)
                v.push_back(v[j]+matrix[i][j]);
            dp.push_back(v);
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        int sum=0;
        for(int i=row1;i<=row2;i++){
            sum=sum+(dp[i][col2+1]-dp[i][col1]);
        }
        return sum;
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */
