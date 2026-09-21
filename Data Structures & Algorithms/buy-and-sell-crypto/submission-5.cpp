class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int left = 0;
        int right = 0;
        int maxProfit = 0;

        // iterate through the entire prices list
        while (right < prices.size()){
            // if the left price is less than the price on the right (profit)
            if (prices[left] < prices[right]){
                // calculate current profit and compare to max profit so far
                int profit = prices[right] - prices[left];
                maxProfit = max(maxProfit, profit);
            }
            // if right > left (cheaper day) so move left ptr to right ptr
            else {
                left = right;
            }
            // move right ptr regardless to search through all days
            right++;
        }
        return maxProfit;
    }
};
