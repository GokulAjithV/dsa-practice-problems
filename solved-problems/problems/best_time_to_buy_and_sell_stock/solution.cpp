class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int min_buy = prices[0] ;
        for(auto it: prices){
            min_buy = min(min_buy,it);
            profit = max(profit,it - min_buy);
        }
        return profit;
    }
};