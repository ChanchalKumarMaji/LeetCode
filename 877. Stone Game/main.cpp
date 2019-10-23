class Solution {
public:
    bool stoneGame(vector<int>& piles) {
        int n = piles.size(); 
        int table[n][n], gap, i, j, x, y, z;
        for (gap = 0; gap < n; ++gap)
        {
            for (i = 0, j = gap; j < n; ++i, ++j)
            {
                x = ((i+2) <= j) ? table[i+2][j] : 0;
                y = ((i+1) <= (j-1)) ? table[i+1][j-1] : 0;
                z = (i <= (j-2))? table[i][j-2]: 0;
 
                table[i][j] = max(piles[i] + min(x, y), piles[j] + min(y, z)); 
            }
        }
        int alex = table[0][n-1];
        int lee = accumulate(piles.begin(), piles.end(), 0)-alex;
        
        return alex>lee; 
    }
};
