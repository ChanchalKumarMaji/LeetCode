class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int l=nums.size(),i;
        map<int,int> m;
        
        for(i=0;i<l;i++){
            if(m.count(target-nums[i])==0)
                m[nums[i]]=i;
            else
                break;
        }
        return vector<int>({i,m[target-nums[i]]});
    }
};
