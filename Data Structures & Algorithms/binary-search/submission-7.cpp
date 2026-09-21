class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;

        while (left <= right){
            int middle = left + ((right - left) /2);

            // middle is used to index the middle of the array and find the value at that pos.
            if (nums[middle] > target){
                right = middle - 1;
            } else if(nums[middle] < target){
                left = middle + 1;
            }
            else {
                return middle;
            }
        }
        return -1;
    }
};
