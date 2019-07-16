class Solution {
public:
    string customSortString(string S, string T) {
        int d[26];
        char c;
        string str="";
        int l1=S.length();
        int l2=T.length();
        int i,k;
        for(i=0;i<26;i++)
            d[i]=0;
        for(i=0;i<l2;i++){
            k=(int)T[i] -97; 
            d[k]++; 
        }
        for(i=0;i<l1;i++){
            c=S[i];
            k=(int)c-97;
            
            while(d[k]!=0){
                str=str+c;
                d[k]--;
                }
            }
        for(i=0;i<26;i++){
            while(d[i]!=0){
               str=str+((char)(i+97));
               d[i]--;
        }    
      }      
        
      return str;  
    }
};
