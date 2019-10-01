class Solution {
public:
    int distanceBetweenBusStops(vector<int>& distance, int start, int destination) {
        int total_dist = 0, dist = 0, n = distance.size(), res;
        if(start > destination) swap(start, destination); 
        for(int i=0; i<n; i++) total_dist += distance[i]; 
        for(int i=start; i<destination; i++) dist += distance[i];
        res = min(dist, total_dist-dist);
        return res;
    }
};
