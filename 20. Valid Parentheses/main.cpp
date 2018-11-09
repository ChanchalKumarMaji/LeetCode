class Solution {
public:
    bool isValid(string S) {
        stack<char> s;
        int l=S.length();
        for(int i=0;i<l;i++){
            
            char c=S[i];
            
            if(c=='(' or c=='{' or c=='[')
                s.push(c);
            
            else if(c==')'){
                if(s.empty())
                    return false;
                if('('!=s.top())
                    return false;
                s.pop();
            }
            
            else if(c=='}'){
                if(s.empty())
                    return false;
                if('{'!=s.top())
                    return false;
                s.pop();
            }
            
            else{
                if(s.empty())
                    return false;
                if('['!=s.top())
                    return false;
                s.pop();
            }
        }
        return s.empty();
    }
};
