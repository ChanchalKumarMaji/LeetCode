#define ll long long 
#define F first 
#define S second
#define pb push_back
#define mp make_pair
#define INF 0d3f3f3f3f
#define INFL 0d3f3f3f3f3f3f3f3fLL
 
typedef pair<ll,ll> pi;
int solve(ll cum[],ll n,ll d)
{
	ll besti =9999999999999LL;
 
   priority_queue< pi, vector<pi>, greater<pi> > pq;
 
        pq.push(pi(cum[0], 0));
        for(ll i = 1; i <= n; i++)
        {
            while(!pq.empty() && cum[i] - pq.top().first >= d ){
                besti = min(besti, i - pq.top().second);
                pq.pop();
            }
            pq.push(pi(cum[i], i));
        }
        return besti > n ? -1 : besti;
}

class Solution {
public:
    int shortestSubarray(vector<int>& A, int K) {
        long long n = A.size(),d = K;
    	int ct=0;
        long long cum[n+1];
    	for(long long i=0;i<n;i++){if(A[i]>=0)ct++;}
    		cum[0]=0;
    	for(long long i=1;i<=n;i++)cum[i]=A[i-1]+cum[i-1];	
 
    	if(d>0 and ct==0)
            return -1;
    	else if(d<=0)
    	{	
          
          	int flag=-1;
          	for(int i=0;i<n;i++)
          		if(A[i]>=d){flag=1;break;}
          	return flag;
          	
        }
        else
        {
          return solve(cum,n,d);
        }
    }
};
