class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        int dx = coordinates[1][0] - coordinates[0][0];
        int dy = coordinates[1][1] - coordinates[0][1];
        
        for(int i=2; i<coordinates.size(); i++){
            int dx_ = coordinates[i][0] - coordinates[i-1][0];
            int dy_ = coordinates[i][1] - coordinates[i-1][1];
            if(((dx*dy_) != (dx_*dy))) return false;
        }
        return true;
    }
};
