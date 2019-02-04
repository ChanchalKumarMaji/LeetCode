int titleToNumber(char* s) {
    int length = strlen(s);
    int res = 0;
    int f = 1;
    for(int i=length-1; i>=0; i--){
        res += (s[i]-'A'+1)*f;
        f = f*26;
    }
    return res; 
}
