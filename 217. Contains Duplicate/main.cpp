class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int,int> m;
        for(int num:nums){
            if(m.count(num)==0)
                m[num]=1;
            else
                return true;
        }
        return false;
    }
};
