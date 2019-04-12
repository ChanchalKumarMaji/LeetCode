class Solution {
public:
    char findTheDifference(string s, string t) {
        int c=0;
        
        for(int i=0;i<(s+t).length();i++)
            c=c^ (s+t)[i];
        
        return (char)c;
    }
};
