class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        //next_permutation(nums.begin(), nums.end());
        
        int i = nums.size()-1;
        while(i > 0 && nums[i-1] >= nums[i]){
            i--; 
        } 
        //cout<<i<<endl;
        if(i<=0)
            reverse(nums.begin(), nums.end()); 
        else{
            int j = nums.size()-1;  
            while(nums[j] <= nums[i-1]){
                j--; 
            }
            //cout<<j<<endl; 
            
            int temp;
            
            temp = nums[j];
            nums[j] = nums[i-1];
            nums[i-1] = temp; 
            
            j = nums.size()-1;
            while(i < j){
                temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                i++;
                j--; 
            }
        }    
        
        
        
    }
};
