typedef long long LL;

class Solution {
    LL gcd(LL a, LL b)
    {
        if (a == 0)
            return b;
        return gcd(b % a, a);
    }
    LL BS(LL a, LL b, LL n)
    {
        LL high,low,mid,cnt,lcm;
        low = 1;
        high = 1e18;
        lcm = (a * b) / gcd(a, b);

        while(low <= high)
        {
            mid = (low + high) / 2;
            cnt = (mid / a) + (mid / b) - (mid / lcm);

            if(cnt < n)
                low = mid + 1;
            if(cnt > n)
                high = mid - 1;
            if(cnt == n)
                break;
        }
        while(mid % a && mid % b)
            mid--;
        return mid;
    }
public:
    int nthMagicalNumber(int N, int A, int B) {
        LL p = 1000000007;
        return BS(A, B, N)%p;
    }
};
