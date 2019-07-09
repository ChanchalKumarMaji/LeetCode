class Solution {
public:
    int countPrimeSetBits(int L, int R) {
        /*vector<int> prime(32,1);
        prime[0]=0;
        prime[1]=0;
        int p=2;
        while(p*p<=31){
            if(prime[p]){
                for(int i=p*2;i<=31;i=i+p)
                    prime[i]=0;
            }
            p++;
        }
        */
        int prime[]={0,0,1,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1};
        int count=0;
        for(int i=L;i<=R;i++){
            if(prime[__builtin_popcount(i)])
                count++;
        }
        return count; 
        
    }
};
