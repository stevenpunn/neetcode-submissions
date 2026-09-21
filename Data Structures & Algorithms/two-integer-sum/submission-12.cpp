class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // maps value -> index 
        unordered_map<int, int> indices;

        // for every num in nums, record where it lives
        for(int i = 0; i < nums.size(); i++){
            indices[nums[i]] = i;
        }

        for(int i = 0; i < nums.size(); i++){
            int diff = target - nums[i];    // value = value - index's value

            // checks if value diff exists anywhere in nums
            // indices[diff] gives the index of diff, compare against index
            // this is an index vs index comparison
            if(indices.count(diff) && indices[diff] != i){
                return {i, indices[diff]};
            }
        }
        return {};
    }
};
