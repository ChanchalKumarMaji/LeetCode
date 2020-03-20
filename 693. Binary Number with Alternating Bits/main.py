class Solution {
public:
    bool hasAlternatingBits(int n) {
        int b = n & 1;
        n = n >> 1;
        int bb;
        
        while(n){
            bb = n & 1;
            n = n >> 1;
            if(b != bb)
                b = bb;
            else
                return false;
        }
        return true;
    }
};
