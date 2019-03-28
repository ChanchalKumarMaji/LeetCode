class Solution {
public:
    bool isPowerOfFour(int n) {
        int count=0;
        if(n<=0)
            return false;
        if(n && !(n & (n-1))){
            while(n>1){
                n >>=1;
                count+=1;
            }
        return (count%2==0)?true:false;    
        }
        
        return false;
        
        
    }
};
