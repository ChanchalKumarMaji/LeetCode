typedef pair<int, int> ii;
class Solution {
public:
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        int res = 0;
        map<ii, int> dict;
        for(int i=0; i<dominoes.size(); i++){
            int a = dominoes[i][0], b = dominoes[i][1];
            ii key = {min(a, b), max(a, b)};
            dict[key] += 1;
        }
        for(auto it = dict.begin(); it != dict.end(); it++){
            int value = it->second;
            res += value*(value-1) / 2;
        }
        return res;
    }
};

