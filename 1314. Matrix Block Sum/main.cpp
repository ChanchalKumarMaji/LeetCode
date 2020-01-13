class Solution {
    vector<vector<int>> sums;
    int row = 0, col = 0;
public:
    void sum(vector<vector<int>>& matrix) {
        row = matrix.size();
        col = row>0 ? matrix[0].size() : 0;
        sums.assign(row+1, vector<int>(col+1, 0));
        for(int i=1; i<=row; i++){
            for(int j=1; j<=col; j++){
                sums[i][j] = sums[i-1][j] + sums[i][j-1] - sums[i-1][j-1] + matrix[i-1][j-1];
            }
        }
    }
    int sumRegion(int row1, int col1, int row2, int col2) {
        row1++; col1++; row2++; col2++;
        return sums[row2][col2] - sums[row1-1][col2] - sums[row2][col1-1] + sums[row1-1][col1-1];
    }
    vector<vector<int>> matrixBlockSum(vector<vector<int>>& mat, int K) {
        sum(mat);
        vector<vector<int>> res;
        res.assign(row, vector<int>(col, 0));
        for(int i=0; i<row; i++){
            for(int j=0; j<col; j++){
                res[i][j] = sumRegion(max(i-K, 0), max(j-K, 0), min(i+K, row-1), min(j+K, col-1));
            }
        }
        return res;
    }
};
