class Solution {
public:
    string convertToTitle(int n) {
        string res = "";
        while(n != 0){
            int rem = n%26;
            n = n/26;
            if(rem == 0){
                res = "Z" + res;
                n--;
            }
            else{
                res = (char)(rem + 64) + res; 
            }
        }
        return res; 
    }
};
