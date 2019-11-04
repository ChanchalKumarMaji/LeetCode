typedef vector<int> vi;
class Solution {
    vi p;
public:
    int findSet(int i){
        return (p[i] == i) ? i : (p[i] = findSet(p[i]));
    }
    bool isSameSet(int i, int j){
        return findSet(i) == findSet(j);
    }
    void unionSet(int i, int j){
        int x = findSet(i), y = findSet(j);
        if(!isSameSet(i, j)){
            p[x] = y;
        }
    }
    
    bool equationsPossible(vector<string>& equations) {
        p.assign(26, 0); for(int i=0; i<26; i++) p[i] = i;
        
        for(auto equation : equations){
            if(equation[1] == '='){
                unionSet(equation[0]-'a', equation[3]-'a');
            }
        }
        for(int i=0; i<26; i++) findSet(i);
        for(auto equation : equations){
            if(equation[1] == '!'){
                int ac1 = equation[0] - 'a';
                int ac2 = equation[3] - 'a';
                if(p[ac1] == p[ac2]) return false;
            }
        }
        return true;
    }
};
