class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int R = matrix.size();
        if(R == 0)
            return false; 
        int C = matrix[0].size(); 
        int I = 0, J = C-1;
        while(I<R && J>=0){
            if(matrix[I][J] == target)
                return true; 
            if(matrix[I][J] < target)
                I++;
            else if(matrix[I][J] > target)
                J--; 
        }
        return false; 
    }
};
