class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_so_far = nums[0], curr_max = nums[0], start = 0, end = 0;
        for(int i=1; i<nums.size(); i++){
            curr_max = max(curr_max+nums[i], nums[i]);
            max_so_far = max(max_so_far, curr_max);
        }
        return max_so_far;
    }
};
