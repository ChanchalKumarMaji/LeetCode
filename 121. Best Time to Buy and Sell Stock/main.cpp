class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size()<=1)
            return 0;
        int min_price=prices[0],max_profit=0;
        for(int i=0;i<prices.size()-1;i++){
            min_price=min(min_price,prices[i]);
            max_profit=max(max_profit,prices[i+1]-min_price);
        }
        return max_profit; 
    }
};
