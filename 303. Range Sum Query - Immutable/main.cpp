class NumArray {
public:
    
    vector<int> dp;
    
    NumArray(vector<int> nums):dp(nums.size()+1, 0) {
        partial_sum(nums.begin(),nums.end(),dp.begin()+1);
    }
    
    int sumRange(int i, int j) {
        return dp[j+1]-dp[i];
    }
    
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(i,j);
 */
