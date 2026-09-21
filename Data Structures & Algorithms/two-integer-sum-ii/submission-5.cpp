class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        // use 2 pointers
        // if the sum is too large, move the right pointer
        // if the sum is too small, move the left pointer
        int left = 0;
        int right = numbers.size()- 1; 

        while (left < right){
            int currentSum = numbers[left] + numbers[right];

            if (currentSum < target){
                left++;
            }
            else if (currentSum > target){
                right--;
            }
            else {
                return {left+1, right+1};
            }
        }
        return {};
    }
};
