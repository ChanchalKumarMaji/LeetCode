class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        map<int,int> m;
        int l=nums.size();
        for(int i=0;i<l;i++){
            if(m.count(nums[i])==0)
                m[nums[i]]=i;
            else{
                if(i-m[nums[i]]<=k)
                    return true;
                m[nums[i]]=i;
            }
                
        }
        return false;
    }
};
