class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // left is buy day
        // right is sell day
        int left = 0;
        int right = 1;
        int maxProfit = 0;

        while (right < prices.size()){
            // if right > left, we can make a profit so update max
            if (prices[left] < prices[right]){
                int profit = prices[right] - prices[left];
                maxProfit = max(maxProfit, profit);
            }
            else {
                // if left > right, move the buy day since we found a cheaper price
                left = right;
            }
            // move right to next day to keep searching
            right++;
        }
        return maxProfit;
    }
};
