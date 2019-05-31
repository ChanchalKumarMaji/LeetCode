class Solution {
public:
    int largestRectangleArea(vector<int> &height) {
        
        int maxArea = 0;
        height.push_back(0);
        stack<int> s;
        
        for(int i = 0; i < height.size(); i++)
        {
            while(!s.empty() && height[s.top()] >= height[i])
            {
                int h = height[s.top()];
                s.pop();
                
                int sidx = !s.empty() ? s.top() : -1;
                if(h * (i-sidx-1) > maxArea)
                    maxArea = h * (i-sidx-1);
            }
            s.push(i);
        }
        
        return maxArea; 
    }
};
