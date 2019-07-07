typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
#define INF 1000000000

class Solution {
    vector<vii> AdjList;
    bool notFilled(vi dist){
        for(int i=0; i<dist.size(); i++){
            if(dist[i] == INF)
                return true;
        }
        return false; 
    }
public:
    int networkDelayTime(vector<vector<int>>& times, int N, int K) {
        AdjList.assign(N, vii());
        for(int i=0; i<times.size(); i++){
            int u = times[i][0];
            int v = times[i][1];
            int w = times[i][2];
            u--;
            v--; 
            AdjList[u].push_back(ii(v, w));
        }
        vi dist(N, INF);
        K--;
        dist[K] = 0;
        priority_queue<ii, vector<ii>, greater<ii> > pq; 
        pq.push(ii(0, K));
        while(!pq.empty()){
            ii front = pq.top(); pq.pop();
            int d = front.first, u = front.second;
            if(d>dist[u])
                continue;
            for(int j=0; j<AdjList[u].size(); j++){
                ii v = AdjList[u][j];
                if(dist[u] + v.second < dist[v.first]){
                    dist[v.first] = dist[u] + v.second;
                    pq.push(ii(dist[v.first], v.first));
                }
            }
        }
        
        if(AdjList[K].size() == 0 || notFilled(dist))
            return -1;
        
        int res = 0;
        for(int i=0; i<N; i++){
            if(dist[i] != INF){
                res = max(res, dist[i]);
            }    
        }
        
        return res;
    }
};
