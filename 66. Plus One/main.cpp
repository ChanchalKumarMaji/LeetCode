class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
     
        int length=digits.size(),i,flag=1,d=1,r;
        for(i=0;i<length;i++){
            if(digits[i]!=9)
                flag=0;
        }
        
        vector<int> v;
        
        if(flag){
            v.push_back(1);
            for(i=0;i<length;i++)
                v.push_back(0);
            return v;
        }
        else
        {
            for(i=length-1;i>=0;i--){
                d = (d+digits[i]);
                r = d%10;
                digits[i] = r;
                d = d/10; 
            }
            
            return digits;
        }
    }
};
