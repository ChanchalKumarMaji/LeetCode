class Solution {
public:
    int trailingZeroes(int n) {
        int p5=0;
        while(n!=0){
            n=n/5;
            p5=p5+n;
        }
    return p5;    
    }
};
