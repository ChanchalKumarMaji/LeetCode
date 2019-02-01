class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l=0,r=numbers.size()-1;
        while(l<r){
            if(numbers[l]+numbers[r]==target)
                break;
            else if(numbers[l]+numbers[r]>target)
                r--;
            else
                l++; 
        }
        vector<int> v;
        v.push_back(l+1);
        v.push_back(r+1);
        return v;
    }
};
