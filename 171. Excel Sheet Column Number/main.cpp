class Solution {
public:
    int titleToNumber(string s) {
        long long int l=s.length();
        long long int sum=0;
        for(long long int i=l-1;i>=0;i--){
            int k=(int)s[i]-64;
            sum=sum+(int)(k*pow(26,l-i-1));
        }
        return sum;
    }
};
