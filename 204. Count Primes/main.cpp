class Solution {
public:
    bool isPrime(int n){
        if(n<=1)
            return false;
        if(n==2 or n==3)
            return true;
        if(n%2==0 or n%3==0)
            return false;
        for(int i=5;i<=sqrt(n);i=i+6){
            if(n%i==0 or n%(i+2)==0)
                return false;
        }
        return true;
    }
    int countPrimes(int n) {
        int count=0;
        for(int i=1;i<n;i++)
            if(isPrime(i))
                count++;
        return count;
    }
};
