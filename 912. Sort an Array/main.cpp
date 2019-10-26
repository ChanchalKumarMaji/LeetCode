class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        int count[100001], p = 0;
        for(int i=0; i<100001; i++) count[i] = 0;
        for(int num : nums) count[num + 50000]++;
        for(int i=0; i<100001; i++){
            int c = count[i]; 
            for(int j=0; j<c; j++) nums[p++] = i-50000;
        }
        return nums;
    }
};
