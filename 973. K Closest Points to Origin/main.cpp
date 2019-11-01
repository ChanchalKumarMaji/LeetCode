int square(vector<int> p){
    return p[0]*p[0] + p[1]*p[1];
}
struct MyClass{
    bool operator () (vector<int> i, vector<int> j){
        return square(i) < square(j);
    }
}obj;

class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
        sort(points.begin(), points.end(), obj);
        vector<vector<int>> res;
        for(int i=0; i<K; i++) res.push_back(points[i]);
        return res;
    }
};
