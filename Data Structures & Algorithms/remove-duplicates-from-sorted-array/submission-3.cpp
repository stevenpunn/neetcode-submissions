class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // since the array is sorted, we can compare element with the prev element
        // start left = 1 since the first element is always unique
        int left = 1;
        for (int right = 1; right < nums.size(); right++){
            // if the next value is different from the prev, it is unique
            if (nums[right] != nums[right-1]){
                // copy it to the position left and increment by 1
                // essentially, this is shrinking the list and copying values to the left
                // left is tracking unqiue values, so we return left because it stores only the unique values 
                // so left only advances if the index is unique
                nums[left++] = nums[right];
            }
        }
        return left;
    }
};