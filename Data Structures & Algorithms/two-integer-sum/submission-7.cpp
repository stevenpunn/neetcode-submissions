class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // start with an unordered map (hashmap)
        unordered_map<int, int> indices;

        for(int i=0; i < nums.size(); i++){
            indices[nums[i]] = i;
        }

        for (int i=0; i < nums.size(); i++){
            int diff = target - nums[i];
            if (indices.count(diff) && indices[diff] != i){
                return {i, indices[diff]};
            }
        }
        return {};
    }
};
