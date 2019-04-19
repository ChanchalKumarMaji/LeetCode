class Solution {
public:
    string addStrings(string num1, string num2) {
        int l1=num1.length();
        int l2=num2.length();
        int i1,i2,d;
        
        i1=l1-1;
        i2=l2-1;
        d=0;
        string st="";
        while(i1>=0 and i2>=0){   
            d=d+ num1[i1]-'0' + num2[i2]-'0'; 
            st=char((d%10) +'0')+st;
            d=d/10;
            i1--;
            i2--;
        }
        
        
        if(l1==l2){
            if(d)
                st=char(d +'0')+st;
            return st;
        }
        else if(l1<l2){
            while(i2>=0){
                d=d+ num2[i2]-'0';
                st=char(d%10 +'0') +st;
                d=d/10;
                i2--;
            }
            if(d)
                st=char(d +'0') +st;
            return st;
        }
        else{
            while(i1>=0){
                d=d+ num1[i1]-'0';
                st=char(d%10 +'0') +st;
                d=d/10;
                i1--;
            }
            if(d)
                st=char(d +'0') +st;
            return st;
        }
        
    }
};
