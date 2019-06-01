class Solution {
public:
    int largestRectangleArea(vector<int> &height) {
        int maxArea=0;
        stack<int> s;
        height.push_back(0);
        
        for(int i=0; i<height.size(); i++){
            while(!s.empty() && height[s.top()]>=height[i]){
                int h=height[s.top()];
                s.pop();
                
                int sidx=!s.empty() ? s.top():-1;
                
                maxArea=max(maxArea, h*(i-sidx-1));
            }
            s.push(i);
        }
        return maxArea;
    }
    
    int maximalRectangle(vector<vector<char>>& matrix) {
        int maxArea=0;
        int m=matrix.size();
        if(m==0) return maxArea;
        int n=matrix[0].size();
        vector<int> height(n, 0); 
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(matrix[i][j]=='0')
                    height[j] = 0;
                else
                    height[j] += 1;
            }
            maxArea=max(maxArea, largestRectangleArea(height));
        }
        return maxArea;
    }
};
