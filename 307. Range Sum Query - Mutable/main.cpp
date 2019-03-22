class NumArray {
    
private:    
    
    const int N = 1e5;
    int n;
    vector<int> t = vector<int>(2*N); 

public:
    
    void build(){
        for(int i=n-1;i>0;i--)  t[i] = t[i<<1] +t[i<<1 | 1];     
    }
    
    NumArray(vector<int> nums) {
        n=nums.size();
        for(int i=0; i<n; i++) t[n+i]=nums[i];
        build();
    }
    
    void update(int p, int value) {
        for(t[p += n] = value; p>1; p>>=1) t[p>>1] = t[p] +t[p^1];
    }
    
    int sumRange(int l, int r) {
        r+=1;
        int res=0;
        for(l += n, r += n; l<r; l >>= 1, r >>= 1){
            if(l&1) res += t[l++];
            if(r&1) res += t[--r];
        }
        return res;
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(i,val);
 * int param_2 = obj.sumRange(i,j);
 */
