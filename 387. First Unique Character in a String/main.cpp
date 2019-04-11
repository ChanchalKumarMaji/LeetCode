class Solution {
public:
    int firstUniqChar(string s) {
        int l=s.length(),i;
        map<char,int> m;
        
        for(i=0;i<l;i++){
            if(m.count(s[i])==0)
                m[s[i]]=i;
            else
                m[s[i]]=-1;
        }
        for(i=0;i<l;i++){
            if(m[s[i]]!=-1)
                return m[s[i]];
        }
        return -1;
    }
};
