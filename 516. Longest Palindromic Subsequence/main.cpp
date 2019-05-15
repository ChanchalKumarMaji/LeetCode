class Solution{
public:
    int longestPalindromeSubseq(string s){
        
        int length,i,j,k,count;
        
        length=s.length();
        int table[length][length];
        
        for(i=1;i<length;i++)
            table[i][i-1]=0;
        
        for(i=0;i<length;i++)
            table[i][i]=1;
             
    
         
        
        count=1;
        for(k=length-1;k>0;k--){
            for(i=0;i<k;i++){        
                j=i+count;
                if(s[i]!=s[j])
                    table[i][j]=(table[i][j-1]>table[i+1][j])?table[i][j-1]:table[i+1][j];
                else
                    table[i][j]=table[i+1][j-1] + 2;    
                }    
            count=count+1;    
            }    

        return table[0][length-1];        
        }
};
