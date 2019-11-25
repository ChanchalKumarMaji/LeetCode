typedef vector<int> vi;
struct MyClass{
    bool operator () (char i, char j){
        return i>j;
    }
}obj;
class Solution {
    vi p;
public:
    void UnionFind(int N){
        p.assign(N, 0); for(int i=0; i<N; i++) p[i] = i;
    }
    int findSet(int i){
        return (p[i] == i) ? i : (p[i] = findSet(p[i]));
    }
    bool isSameSet(int i, int j){
        return findSet(i) == findSet(j);
    }
    void unionSet(int i, int j){
        int x = findSet(i), y = findSet(j);
        if(!isSameSet(x, y)){
            p[x] = y;
        }
    }
    
    string smallestStringWithSwaps(string s, vector<vector<int>>& pairs) {
        int N = s.length(); UnionFind(N);
        for(auto pair : pairs){
            unionSet(pair[0], pair[1]);
        }
        map<int, vector<char>> d;
        for(int i=0; i<N; i++){
            findSet(i);
            d[p[i]].push_back(s[i]);
        }
        map<int, vector<char>> :: iterator it;
        for(it=d.begin(); it!=d.end(); it++){
            vector<char> vc = it->second;
            sort(vc.begin(), vc.end(), obj);
            d[it->first] = vc;
        }
        string res = "";
        for(int i=0; i<N; i++){
            res += d[p[i]].back();
            d[p[i]].pop_back();
        }
        
        return res;
    }
};
